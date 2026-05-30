from fastapi import APIRouter
from app.ml.emotion import detect_emotions

router = APIRouter()

@router.post("/emotion")
def analyze_emotion(data: dict):

    text = data.get("text")

    emotions = detect_emotions(text)

    return {
        "text": text,
        "emotions": emotions
    }