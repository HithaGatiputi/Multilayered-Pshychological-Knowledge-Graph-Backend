from schema import driver

def load_emotions():

    emotions = [
        {"name": "anxiety", "valence": "negative"},
        {"name": "joy", "valence": "positive"},
        {"name": "sadness", "valence": "negative"},
        {"name": "anger", "valence": "negative"},
        {"name": "fear", "valence": "negative"},
    ]

    with driver.session() as session:

        for e in emotions:

            session.run("""
            MERGE (em:Emotion {name:$name})
            SET em.valence = $valence
            """, e)

    print("Emotions loaded.")

def load_cognitions():

    cognitions = [
        {"name":"catastrophizing"},
        {"name":"overgeneralization"},
        {"name":"mind_reading"},
        {"name":"personalization"},
    ]

    with driver.session() as session:

        for c in cognitions:

            session.run("""
            MERGE (c:Cognition {name:$name})
            """, c)

    print("Cognitions loaded.")

def load_people():

    people = [
        {"id":1, "name":"Alice"},
        {"id":2, "name":"Bob"},
        {"id":3, "name":"Charlie"},
    ]

    with driver.session() as session:

        for p in people:

            session.run("""
            MERGE (p:Person {id:$id})
            SET p.name = $name
            """, p)

    print("People loaded.")
def create_relationships():

    with driver.session() as session:

        session.run("""
        MATCH (a:Person {name:'Alice'}),
              (b:Person {name:'Bob'})
        MERGE (a)-[:FRIEND_OF]->(b)
        """)

        session.run("""
        MATCH (a:Person {name:'Alice'}),
              (e:Emotion {name:'anxiety'})
        MERGE (a)-[:FEELS]->(e)
        """)

        session.run("""
        MATCH (b:Person {name:'Bob'}),
              (c:Cognition {name:'catastrophizing'})
        MERGE (b)-[:HAS_BELIEF]->(c)
        """)

    print("Relationships created.")

if __name__ == "__main__":

    load_emotions()
    load_cognitions()
    load_people()
    create_relationships()
