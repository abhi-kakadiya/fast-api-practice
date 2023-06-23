from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.database.setup import get_db
from app.schemas.schema_entry import EntryBase,EntryDisplay,EntryUpdate
from app.models.models import EntryDB
from fastapi.encoders import jsonable_encoder
from typing import List

entry = APIRouter(
    prefix="/entry",
    tags=["Entry"]
)

@entry.post("/add")
def create_entry(request: EntryBase, db: Session = Depends(get_db)):
    new_entry= EntryDB(**request.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    status.HTTP_201_CREATED
    return new_entry


@entry.get("/all",response_model=List[EntryDisplay])
def get_all_entries(db: Session = Depends(get_db)):
    all_entries =  db.query(EntryDB).all()
    return all_entries


@entry.get("/{id}",response_model=EntryDisplay)
def get_entry_by_id(id:int,db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == id).first()
    if not entry:
        return {"message":f"Entry with id {id} not found"}
    else:
        status.HTTP_200_OK
        return entry
    
@entry.put("/update/{id}")
def update_entry_by_id(id:int,request:EntryBase, db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == id).first()
    if not entry:
        return {"message":f"Entry with id {id} not found"}
    else:
        update_data = request.dict(exclude_unset=True) 
        db.query(EntryDB).filter(EntryDB.id == id).update(update_data)
        db.commit()
        return {"message": f"Entry with id {id} Updated successfully"}  

@entry.delete("/delete/{id}")
def delete_entry_by_id(id:int, db: Session = Depends(get_db)):
    entry = db.query(EntryDB).filter(EntryDB.id == id)
    if not entry:
       return {"message":f"Entry with id {id} not found"}
    else:
        status.HTTP_204_NO_CONTENT
        entry.delete()
        db.commit()
        return {"message":f"Entry with id {id} Deleted successfully"}
        


