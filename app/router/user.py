from fastapi import Depends, APIRouter,status
from sqlalchemy.orm import Session
from app.database.setup import get_db
from app.schemas.schema_user import UserBase,UserDisplay,UserUpdate
from app.models.models import UserDB
from fastapi.encoders import jsonable_encoder
from typing import List

user = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user.post("/add")
def create_user(request: UserBase, db: Session = Depends(get_db)):
    new_user = UserDB(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    status.HTTP_201_CREATED
    return new_user


@user.get("/all",response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    all_user =  db.query(UserDB).all()
    return all_user


@user.get("/{id}",response_model=UserDisplay)
def get_user_by_id(id:int,db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        return {"message":f"Competition with id {id} not found"}
    else:
        status.HTTP_200_OK
        return user
    
@user.put("/update/{id}")
def update_user_by_id(id:int,request:UserBase, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        return {"message":f"Competition with id {id} not found"}
    else:
        update_data = request.dict(exclude_unset=True) 
        db.query(UserDB).filter(UserDB.id == id).update(update_data)
        db.commit()
        return {"message": f"User with id {id} Updated successfully"}  

@user.delete("/delete/{id}")
def delete_user_by_id(id:int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == id)
    if not user:
        return {"message":f"Competition with id {id} not found"}
    else:
        status.HTTP_204_NO_CONTENT
        user.delete()
        db.commit()
        return {"message":f"User with id {id} Deleted successfully"}
        


