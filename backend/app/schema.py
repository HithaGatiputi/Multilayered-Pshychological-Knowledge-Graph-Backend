from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password123")

driver = GraphDatabase.driver(URI, auth=AUTH)

def create_schema():

    with driver.session() as session:

        session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (p:Person)
        REQUIRE p.id IS UNIQUE
        """)

        session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (e:Emotion)
        REQUIRE e.name IS UNIQUE
        """)

        session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (c:Cognition)
        REQUIRE c.name IS UNIQUE
        """)

        session.run("""
        CREATE CONSTRAINT IF NOT EXISTS
        FOR (ev:Event)
        REQUIRE ev.id IS UNIQUE
        """)

        print("Schema created successfully.")

if __name__ == "__main__":
    create_schema()