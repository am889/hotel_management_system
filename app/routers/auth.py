from fastapi import APIRouter,Body,Path,Depends,HTTPException
from starlette import status
from models import *
import methods
import schemas
from database import db_dependency
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(prefix='/auth',tags=["Authentication"])

bcrypt_context =CryptContext(schemes=['bcrypt'],deprecated='auto')
@router.post("/add",status_code=status.HTTP_201_CREATED)
async def add_users(db:db_dependency,userrequest:schemas.UserRequest):
    user_model = Users(**userrequest.model_dump())
    user_model.password=bcrypt_context.hash(userrequest.password)
    db.add(user_model)
    db.commit()
    return user_model

@router.post('/token',response_model=schemas.Token)
async def login_for_access_token(form:Annotated[OAuth2PasswordRequestForm , Depends()],db:db_dependency):
    user= methods.Token(form.username,form.password,db)
    token =user.login_for_access_token()
    return {'access_token':token,'token_type':'bearer'}

    
