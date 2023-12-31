from datetime import datetime
from app.database.setup import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date,ForeignKey


class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthdate = Column(Date)
    gender = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
    competitions = relationship("CompetitionDB", back_populates="user")



class CompetitionDB(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    is_active = Column(Boolean,default=True)
    is_delete = Column(Boolean,default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    description = Column(String)
    participant_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserDB", back_populates="competitions")
    entries = relationship("EntryDB", back_populates="competitions")



class EntryDB(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key = True,index = True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    is_delete = Column(Boolean ,default=False)
    created_at = Column(DateTime, default= datetime.utcnow)
    updated_at = Column(DateTime, default= datetime.utcnow)
    competition_id = Column(Integer , ForeignKey("competitions.id"))

    competitions = relationship("CompetitionDB", back_populates="entries")
