from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
# from methods import Token
DATABASE_URL='sqlite:///./hotel.db'

engine=create_engine(url=DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal= sessionmaker(autoflush=False,autocommit=False,bind=engine)


Base= declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency=Annotated[Session,Depends(get_db)]

