from sqlalchemy.orm import Session
from secrets import token_hex
from . import models
from json import loads


def get_text(db: Session, token: str) -> dict:
    try:
        return db.query(models.Text).filter(models.Text.token == token).first().__dict__
    except AttributeError as e:
        return {"info": "Incorrect token"}


def generate_init_text(db: Session):
    token = token_hex(20)
    db_item = models.Text(token=token)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return token


async def update_text(db: Session, token: str, result: dict):
    db_item = db.query(models.Text).filter(models.Text.token == token).first()
    db_item.result = result
    db_item.status = "done"
    db.commit()
    return db_item
