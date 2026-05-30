from transformers import pipeline
from schema import driver

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def analyze_text(person_name, text):

    result = emotion_classifier(text)

    emotions = result[0]

    highest = max(
        emotions,
        key=lambda x: x["score"]
    )

    detected_emotion = highest["label"]

    confidence = highest["score"]

    print(
        f"Detected emotion: "
        f"{detected_emotion}"
    )

    with driver.session() as session:

        session.run("""
        MATCH (p:Person {name:$name}),
              (e:Emotion {name:$emotion})

        MERGE (p)-[r:FEELS]->(e)

        SET r.ai_generated = true,
            r.intensity = $confidence
        """,
        {
            "name": person_name,
            "emotion": detected_emotion,
            "confidence": confidence
        })

        print(
            f"{person_name} updated "
            f"with {detected_emotion}"
        )

if __name__ == "__main__":

    analyze_text(
        "Charlie",
        "I feel hopeless and exhausted lately"
    )