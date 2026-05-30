from schema import driver

EMOTION_WEIGHTS = {
    "anxiety": 0.8,
    "fear": 0.9,
    "sadness": 0.6,
    "joy": 0.5,
    "anger": 0.7
}

DECAY_FACTOR = 0.5

def propagate_emotion():

    with driver.session() as session:

        query = """
        MATCH path =
        (source:Person)-[:FEELS]->(e:Emotion)

        MATCH chain =
        (source)-[:FRIEND_OF*1..2]->(target:Person)

        RETURN source,target,e,chain
        """

        result = session.run(query)

        for record in result:

            emotion = record["e"]["name"]

            path_length = len(record["chain"])

            base_weight = EMOTION_WEIGHTS.get(emotion, 0.5)

            influence = (
                base_weight *
                (DECAY_FACTOR ** (path_length - 1))
            )

            session.run("""
            MATCH (t:Person {id:$id}),
                  (e:Emotion {name:$emotion})

            MERGE (t)-[r:INFLUENCED_BY]->(e)

            SET r.intensity = $influence
            """,
            {
                "id": record["target"]["id"],
                "emotion": emotion,
                "influence": influence
            })

            print(
                f"{record['target']['name']} "
                f"influenced by {emotion} "
                f"with intensity {round(influence,2)}"
            )

if __name__ == "__main__":
    propagate_emotion()