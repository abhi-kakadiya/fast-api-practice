from typing import Dict,List
from pydantic import BaseModel


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
    name:str
    status:str
    description:str

    class Config:
        orm_mode = True


