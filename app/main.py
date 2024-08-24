from fastapi import FastAPI
import models
import crud
from routers import customer,auth
from database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(customer.router)
app.include_router(auth.router)
app.include_router(crud.router)