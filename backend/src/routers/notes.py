from fastapi import APIRouter, Depends, responses, status, HTTPException
from sqlalchemy.orm import Session
from backend.src.schemas import Note
from backend.src.database import get_db
from backend.src import models

router = APIRouter(
    tags=["note"],
    prefix="/note"
)

@router.post("/", response_model=Note)
def createNote(request:Note, db: Session=Depends(get_db)):
    new_note = models.Note(header=request.header, body=request.body, tags=request.tags)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note