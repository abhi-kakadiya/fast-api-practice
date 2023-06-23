from pydantic import BaseModel


class EntryBase(BaseModel):
    title:str
    topic:str
    state:str
    country:str
    competition_id:int

class EntryUpdate(BaseModel):
    title:str
    topic:str
    state:str
    country:str


class EntryDisplay(BaseModel):
    title:str
    topic:str
    state:str
    country:str

    class Config:
        orm_mode = True