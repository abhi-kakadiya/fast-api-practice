from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.database.setup import get_db
from app.schemas.schema_competition import CompetitionBase, CompetitionDisplay, CompetitionUpdate
from app.models.models import CompetitionDB
from fastapi.encoders import jsonable_encoder


competition = APIRouter(
    prefix="/competition",
    tags=["Competition"]
)


@competition.post("/add")
def create_competition(request: CompetitionBase, db: Session = Depends(get_db)):
    new_competition = CompetitionDB(**request.dict())
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)
    return new_competition


@competition.get("/all", response_model=List[CompetitionDisplay])
def get_all_competitions(db: Session = Depends(get_db)):
    return db.query(CompetitionDB).all()

@competition.get("/{id}", response_model=CompetitionDisplay)
def get_competition_by_id(id:int,db:Session = Depends(get_db)):
    competition = db.query(CompetitionDB).filter(CompetitionDB.id == id).first()
    if not competition:
        return {"message":f"Competition with id {id} not found"}
    else:
        return competition


@competition.put("/update/{id}")
def update_competition_by_id(id:int, request:CompetitionUpdate,db:Session=Depends(get_db)):
    competition = db.query(CompetitionDB).filter(id == CompetitionDB.id).first()
    if competition is None:
        return {"message":f"Competition with id {id} not found"}
    else:
        update_data = request.dict(exclude_unset=True) 
        db.query(CompetitionDB).filter(CompetitionDB.id == id).update(update_data)
        db.commit()
        return {"message": f"Competition with id {id} Updated successfully"}


@competition.delete("/delete/{id}")
def delete_competition_by_id(id:int,db:Session=Depends(get_db)):
    competition = db.query(CompetitionDB).filter(id == CompetitionDB.id).first()
    print(competition)
    if not competition:
        return {"message":f"Competition with id {id} not found"}
    else:
        db.delete(competition)
        db.commit()
        return {"message": f"Competition with id {id} Deleted successfully"}