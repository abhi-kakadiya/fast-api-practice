from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.database.setup import get_db
from app.schemas.schema_entry import EntryBase,EntryDisplay,EntryUpdate
from app.models.models import EntryDB, CompetitionDB
from typing import List

entry = APIRouter(
    prefix="/entry",
    tags=["Entry"]
)

@entry.post("/add", response_model = EntryDisplay)
def create_entry(request: EntryBase, db: Session = Depends(get_db)):
   
    request.title = request.title.casefold()
    request.topic = request.topic.casefold()
    request.state = request.state.casefold()
    request.country = request.country.casefold()
    check_competition = db.query(CompetitionDB).filter(CompetitionDB.id == request.competition_id).first()
    if not check_competition:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {request.competition_id} do not exists"})
    else:
        new_entry= EntryDB(
            title = request.title,
            topic = request.topic,
            state = request.state,
            country = request.country, 
            competition_id = request.competition_id
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return new_entry


@entry.get("/all",response_model=List[EntryDisplay])
def get_all_entries(db: Session = Depends(get_db)):
    all_entries =  db.query(EntryDB).all()
    return all_entries


@entry.get("/{id}",response_model=EntryDisplay)
def get_entry_by_id(id:int,db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == id).first()
    if not entry:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {id} do not exists"})
    else:
        return entry
    
@entry.put("/update/{id}")
def update_entry_by_id(id:int,request:EntryBase, db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == id).first()
    if not entry:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {id} do not exists"})
    else:
        update_data = request.dict(exclude_unset=True) 
        db.query(EntryDB).filter(EntryDB.id == id).update(update_data)
        db.commit()
        return {"message": f"Entry with id {id} Updated successfully"}  

@entry.delete("/delete_all/")
def delete_all_entries(db:Session=Depends(get_db)):
    db.query(EntryDB).delete(synchronize_session=False)
    db.commit()
    return {"message": f"All of the entries Deleted successfully"}
 


@entry.delete("/delete/{id}")
def delete_entry_by_id(id:int, db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == id).first()
    if not entry:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"message":f"Competition with ID {id} do not exists"})
    else:
        status.HTTP_204_NO_CONTENT
        db.delete(entry)
        db.commit()
        return {"message":f"Entry with id {id} Deleted successfully"}
        


