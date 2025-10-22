from fastapi import APIRouter, Depends, responses, status, HTTPException
from sqlalchemy.orm import Session
from backend.src.schemas import Note
from backend.src.database import get_db
from backend.src import models

router = APIRouter(
    tags=["note"],
    prefix="/note"
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def createNote(request:Note, db: Session=Depends(get_db)):
    new_note = models.Note(header=request.header, body=request.body, tags=request.tags) # type: ignore
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.put("/{id}", status_code=status.HTTP_200_OK)
def loadNote(id: int, db:Session=Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id==id).first()

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"note with id={id} note found"
        )
    return note

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def removeNote(id: int, db:Session=Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id==id).first()
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"note with id={id} not found"
        )
    return note
