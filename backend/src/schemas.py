from pydantic import BaseModel
from typing import List, Optional

class Note(BaseModel):
    header: str
    body: str
    tags: List[str]=[]

class ShowNote(BaseModel):
    header: str
    body: str
    class Config():
        orm_mode=True