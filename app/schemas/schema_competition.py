from typing import Dict,List,Optional
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
    name:str
    status:str
    description:str

class CompetitionDisplay(BaseModel):
    name: str
    status: str
    description: str
    user: UserDetails

    class Config:
        orm_mode = True

