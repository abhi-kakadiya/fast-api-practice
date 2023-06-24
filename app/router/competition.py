from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.setup import get_db
from app.schemas.schema_competition import CompetitionBase, CompetitionDisplay, CompetitionUpdate
from app.models.models import CompetitionDB,UserDB



competition = APIRouter(
    prefix="/competition",
    tags=["Competition"]
)


@competition.post("/add", response_model=CompetitionDisplay)
def create_competition(request: CompetitionBase, db: Session = Depends(get_db)):

    request.name = request.name.casefold()
    request.status = request.status.casefold()
    request.description = request.description.casefold()
    check_user = db.query(UserDB).filter(UserDB.id == request.participant_id).first()
    if not check_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"User with ID {request.participant_id} do not exists"})
    else:
        new_competition = CompetitionDB(
            name=request.name,
            status=request.status,
            description=request.description,
            participant_id = request.participant_id
        )
        db.add(new_competition)
        db.commit()
        db.refresh(new_competition)
        return new_competition


@competition.get("/all", response_model=List[CompetitionDisplay])
def get_all_competitions(db: Session = Depends(get_db)):
    competition =  db.query(CompetitionDB).all()
    return competition

@competition.get("/{id}", response_model=CompetitionDisplay)
def get_competition_by_id(id:int,db:Session = Depends(get_db)):
    competition = db.query(CompetitionDB).filter(CompetitionDB.id == id).first()
    if not competition:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {id} do not exists"})
    else:
        return competition


@competition.put("/update/{id}")
def update_competition_by_id(id:int, request:CompetitionUpdate,db:Session=Depends(get_db)):
    competition = db.query(CompetitionDB).filter(id == CompetitionDB.id).first()
    if competition is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {id} do not exists"})
    else:
        update_data = request.dict(exclude_unset=True) 
        db.query(CompetitionDB).filter(CompetitionDB.id == id).update(update_data)
        db.commit()
        return {"message": f"Competition with id {id} Updated successfully"}


@competition.delete("/delete_all/")
def delete_all_competition(db:Session=Depends(get_db)):
    db.query(CompetitionDB).delete(synchronize_session=False)
    db.commit()
    return {"message": f"All of the Competitions Deleted successfully"}
    

@competition.delete("/delete/{id}")
def delete_competition_by_id(id:int,db:Session=Depends(get_db)):
    competition = db.query(CompetitionDB).filter(id == CompetitionDB.id).first()
    print(competition)
    if not competition:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {id} do not exists"})
    else:
        db.delete(competition)
        db.commit()
        return {"message": f"Competition with id {id} Deleted successfully"}