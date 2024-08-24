from fastapi import APIRouter,Body,Path,Depends,HTTPException
from starlette import status
from models import Users
from schemas import UserRequest
from database import db_dependency
from sqlalchemy.orm import sessionmaker,Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from typing import Annotated
from jose import jwt,JWTError
from datetime import timedelta,datetime,timezone


class Token:
    SECRET_KEY='a6ac3b776c00fc7588be67931d8906914f914ae3361828a6fef98ec272765cb9'
    ALGORITHM='HS256'
    oauthbearer=OAuth2PasswordBearer(tokenUrl='auth/token')
    bcrypt_context =CryptContext(schemes=['bcrypt'],deprecated='auto')
    
    
    def __init__(self,email:str,passowrd:str,db):
        self.email=email
        self.password=passowrd
        self.db=db
    

    
    def authenticate_user(self):
        user = self.db.query(Users).filter(Users.email == self.email).first()
        if not user:
            return False
        if not Token.bcrypt_context.verify(self.password,user.password):
            return False
        self.user = user
        return True,self.user
    
    def create_access_token(email:str,user_id:int,expires_delta:timedelta):
        encode={
            'sub':email,'id':user_id}
        expire =datetime.now(timezone.utc) +expires_delta
        encode.update({'exp':expire})
        return jwt.encode(encode,Token.SECRET_KEY,algorithm=Token.ALGORITHM)

    def login_for_access_token(self):
        
        if not self.authenticate_user():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate user")
        
        token=Token.create_access_token(self.user.email,self.user.id,timedelta(minutes=20))
        return token
    
    async def get_current_user(self,token: Annotated[str,Depends(oauthbearer)]):
        try:
            payload=jwt.decode(token,Token.SECRET_KEY,algorithms=[Token.ALGORITHM])
            email:str=payload.get('sub')
            user_id:int =payload.get('id')
            if email is None or user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate user")
            
            return {"email":email,"id":user_id}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate user")
    

user_dependancy =Annotated[Session,Depends(Token.get_current_user)]


# user= Token("alimohamed889@gmail.com","123")
# user.login_for_access_token()