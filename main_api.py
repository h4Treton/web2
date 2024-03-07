from fastapi import FastAPI
from api_schema import UserAdd, User, UserId


from contextlib import asynccontextmanager



app = FastAPI()

@app.get('/')
async def home():
    return {"data":"My data"}

@app.post('/')
async def add_user(user: UserAdd):
    return {"data":user}