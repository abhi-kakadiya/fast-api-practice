from typing import List
from datetime import date
from pydantic import BaseModel, Field

class Competition(BaseModel):
    name:str
    status:str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name:str = Field(description="Full name of User",example="Full name")
    birthdate:date = Field(description="Birthdate of User in given format",example="YYYY-MM-DD")
    gender:str = Field(description="Gender of User",example="Male|Female")

class UserUpdate(BaseModel):
    name:str
    birthdate:date
    gender:str

class UserDisplay(BaseModel):
    name:str 
    birthdate:date
    gender:str
    competitions: List['Competition'] = []

    class Config:
        orm_mode = True
        
