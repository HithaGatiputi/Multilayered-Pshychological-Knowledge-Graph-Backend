from schema import driver

EVENT_EFFECTS = {
    "exam_failure": {
        "emotion": "anxiety",
        "increase": 0.5
    },

    "social_conflict": {
        "emotion": "anger",
        "increase": 0.4
    },

    "loss_event": {
        "emotion": "sadness",
        "increase": 0.6
    }
}

def trigger_event(person_name, event_name):

    if event_name not in EVENT_EFFECTS:
        print("Unknown event")
        return

    event = EVENT_EFFECTS[event_name]

    with driver.session() as session:

        session.run("""
        MATCH (p:Person {name:$name}),
              (e:Emotion {name:$emotion})

        MERGE (p)-[r:FEELS]->(e)

        SET r.intensity =
            coalesce(r.intensity,0) + $increase
        """,
        {
            "name": person_name,
            "emotion": event["emotion"],
            "increase": event["increase"]
        })

        print(
            f"{person_name} affected by "
            f"{event_name}"
        )

if __name__ == "__main__":

    trigger_event(
        "Charlie",
        "exam_failure"
    )