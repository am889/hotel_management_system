from fastapi import APIRouter,Body,Path,Depends,HTTPException
from starlette import status
from models import *
from schemas import RoomRequest,Room,GuestRequest
from database import db_dependency
from methods import user_dependancy
from methods import Token


router = APIRouter(prefix="/guest",tags=["Guests"])



@router.get('/',status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency,user:user_dependancy):
    
    return db.query(Guests).all(),user_dependancy

@router.get('/{guest_id}',status_code=status.HTTP_200_OK)
async def all_users_by_id(db:db_dependency,guest_id:int=Path(gt=0)):
    user= db.query(Guests).filter(Guests.id==guest_id).first()
    if user is not None:
        return user
    raise HTTPException(status_code=404,detail='User Not Found')

@router.put('/update/{guest_id}',status_code=status.HTTP_204_NO_CONTENT)
async def update_guest(db:db_dependency,
                       
                       guest_request:GuestRequest,
                       guest_id:int = Path(gt=0)):
    guest_model = db.query(Guests).filter(Guests.id == guest_id).first()
    if guest_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    
    
    for field,value in guest_request.model_dump().items():
        setattr(guest_model,field,value)
    db.add(guest_model)
    db.commit()
    return {"message": "Guest updated successfully"}

@router.delete('/delete/{guest_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_guest(db:db_dependency,guest_id:int=Path(gt=0)):
    guest_model = db.query(Guests).filter(Guests.id == guest_id).first()
    if guest_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    db.delete(guest_model)
    db.commit()


@router.post('/add',status_code=status.HTTP_201_CREATED)
async def add_guest(guest_request:GuestRequest,db:db_dependency):
    guest_model =Guests(**guest_request.model_dump())
    db.add(guest_model)
    db.commit()