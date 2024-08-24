from fastapi import APIRouter,Body,Path,Depends,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from models import *
from schemas import UserRequest
from database import db_dependency

router = APIRouter(prefix="/user",tags=["Users"])


# @router.post("/add",status_code=status.HTTP_201_CREATED)
# async def add_users(db:db_dependency,userrequest:UserRequest):
#     user_model = Users(**userrequest.model_dump())
#     db.add(user_model)
#     db.commit()

@router.get('/users',status_code=status.HTTP_200_OK)
async def get_all_users(db:db_dependency):
    return db.query(Users).all()

@router.get('/get/{user_id}',status_code=status.HTTP_200_OK)
async def get_user(db:db_dependency,user_id:int):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

@router.put('/update/{user_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db:db_dependency,user_request:UserRequest,user_id :int=Path(gt=0)):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    for field,value in user_request.model_dump().items():
        setattr(user_model,field,value)
    db.add(user_model)
    db.commit()

@router.delete('/delete/{user_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db:db_dependency,user_id:int=Path(gt=0)):
    user_model = db.query(Users).filter(Users.id ==user_id).first()
    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    db.delete(user_model)
    db.commit()
