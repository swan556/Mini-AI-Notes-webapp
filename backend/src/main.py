from fastapi import FastAPI
from backend.src.routers import notes
from backend.src.models import Base
from backend.src.database import engine

app = FastAPI()
Base.metadata.create_all(engine)

app.include_router(notes.router)