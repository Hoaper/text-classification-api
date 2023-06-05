from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from db.database import SessionLocal, engine
from db import models
from db.utils import get_text, generate_init_text, update_text

from ml.detect_text_emotional import DetectTextEmotional

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    version="0.0.1",
    description="API with emotional context detection"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


det = DetectTextEmotional()


class UploadData(BaseModel):
    text: str
    lang: str = "ENG"
    auth_token: str = "TEST123"


@app.post("/upload")
async def upload_text(data: UploadData, db: Session = Depends(get_db)):
    """Endpoint to get upload text to concrete emotional context"""
    token = generate_init_text(db)
    await update_text(db, token, det.get_result(data.text, data.lang))

    return {"info": "Text uploaded", "token": token}


@app.get("/result")
async def result_text_by_token(token: str, db: Session = Depends(get_db)):
    """Get result of text analyze"""
    return get_text(db, token)
