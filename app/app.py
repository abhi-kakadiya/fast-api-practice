from fastapi import FastAPI
from app.router.user import user
from app.router.entry import entry
from app.router.competition import competition
from app.database.setup import Base,engine

app = FastAPI()

app.include_router(user)
app.include_router(entry)
app.include_router(competition)

Base.metadata.create_all(bind=engine)