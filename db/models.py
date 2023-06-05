from abc import ABC

from sqlalchemy import String, Column, Integer
from .database import Base
import json
import sqlalchemy
from sqlalchemy.types import TypeDecorator

SIZE = 512


class ResultType(TypeDecorator, ABC):

    impl = sqlalchemy.Text(SIZE)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class Text(Base):
    __tablename__ = "texts"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    result = Column(ResultType())
    status = Column(String, unique=False, index=False, default="processing")
