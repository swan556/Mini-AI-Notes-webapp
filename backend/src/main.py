from fastapi import FastAPI
from src.routers import notes
from src.models import Base
from src.database import engine

app = FastAPI()
Base.metadata.create_all(engine)

@app.get('/')
def root():
    return {"message": "just a default msg"}
app.include_router(notes.router)