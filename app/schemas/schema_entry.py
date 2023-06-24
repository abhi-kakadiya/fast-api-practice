from pydantic import BaseModel
from typing import Optional, List

class CompetitionDetails(BaseModel):
    name:str
    description:str

    class Config:
        orm_mode = True

class EntryBase(BaseModel):
    title:str
    topic:str
    state:str
    country:str
    competition_id:int

class EntryUpdate(BaseModel):
    title:Optional[str]
    topic:Optional[str]
    state:Optional[str]
    country:Optional[str]

class EntryDisplay(BaseModel):
    title: str
    topic: str
    state: str
    country: str
    competitions: CompetitionDetails

    class Config:
        orm_mode = True
