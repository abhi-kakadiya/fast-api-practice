from typing import List
from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    name:str
    birthdate:date
    gender:str

class UserUpdate(BaseModel):
    name:str
    birthdate:date
    gender:str

class UserDisplay(BaseModel):
    name:str 
    birthdate:date
    gender:str

    class Config:
        orm_mode = True
        
