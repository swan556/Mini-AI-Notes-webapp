from src.database import Base
from sqlalchemy import Column, Integer, String
from typing import List

class Note():
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    header = Column(String)
    body = Column(String)
    tags = List[String]