from fastapi import FastAPI
from app.api.test_graph import router as graph_router
from app.api.emotion import router as emotion_router

app = FastAPI()

app.include_router(graph_router)
app.include_router(emotion_router)

@app.get("/")
def root():
    return {"message": "PsycheGraph AI Running"}

from fastapi.middleware.cors import CORSMiddleware
from app.graph.db import driver

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/graph-data")
def graph_data():

    with driver.session() as session:

        result = session.run("""
        MATCH (n)-[r]->(m)

        RETURN
            n.name as source,
            type(r) as relationship,
            m.name as target
        """)

        data = []

        for record in result:

            data.append({
                "source": record["source"],
                "relationship": record["relationship"],
                "target": record["target"]
            })

        return data
    
