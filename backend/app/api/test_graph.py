from fastapi import APIRouter
from app.graph.db import driver

router = APIRouter()

@router.get("/test-graph")
def test_graph():

    with driver.session() as session:

        result = session.run("""
        MATCH (n)
        RETURN n LIMIT 10
        """)

        data = [record["n"] for record in result]

        return {
            "nodes": data
        }