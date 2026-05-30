from schema import driver

EMOTION_RISK = {
    "anxiety": 8,
    "fear": 9,
    "sadness": 7,
    "anger": 6,
    "joy": 2
}

COGNITION_RISK = {
    "catastrophizing": 8,
    "overgeneralization": 6,
    "mind_reading": 7,
    "personalization": 5
}

def calculate_risk():

    with driver.session() as session:

        query = """
        MATCH (p:Person)

        OPTIONAL MATCH (p)-[:FEELS]->(e:Emotion)

        OPTIONAL MATCH (p)-[:HAS_BELIEF]->(c:Cognition)

        OPTIONAL MATCH (p)-[i:INFLUENCED_BY]->(:Emotion)

        RETURN p,e,c,sum(i.intensity) as influence
        """

        result = session.run(query)

        for record in result:

            person = record["p"]["name"]

            emotion = (
                record["e"]["name"]
                if record["e"] else None
            )

            cognition = (
                record["c"]["name"]
                if record["c"] else None
            )

            influence = (
                record["influence"]
                if record["influence"] else 0
            )

            emotion_score = EMOTION_RISK.get(emotion, 0)

            cognition_score = COGNITION_RISK.get(cognition, 0)

            influence_score = influence * 10

            total_risk = (
                emotion_score +
                cognition_score +
                influence_score
            )

            session.run("""
            MATCH (p:Person {name:$name})

            SET p.risk_score = $risk
            """,
            {
                "name": person,
                "risk": round(total_risk,2)
            })

            print(
                f"{person} risk score: "
                f"{round(total_risk,2)}"
            )

if __name__ == "__main__":
    calculate_risk()