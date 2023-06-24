from typing import List,Optional
from pydantic import BaseModel

class UserDetails(BaseModel):
    name: str
    gender: str

    class Config:
        orm_mode = True

class CompetitionBase(BaseModel):
    name:str
    status:str
    description:str
    participant_id:int


class CompetitionUpdate(BaseModel):
    name:Optional[str]
    status:Optional[str]
    description:Optional[str]


class EntryDetails(BaseModel):
    title:str
    topic:str
    class Config:
        orm_mode = True


class CompetitionDisplay(BaseModel):
    name: str
    status: str
    description: str
    user: UserDetails
    entries: List[EntryDetails] = []

    class Config:
        orm_mode = True

