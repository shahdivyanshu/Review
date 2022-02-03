from asyncio.log import logger
from fastapi import FastAPI
from routers import app
from db.database import engine
from db import get_data
from db import models
from typing import List
from pydantic import BaseModel
app=FastAPI()
import numpy as np

class return_type(BaseModel):
    ids:list[int]
#app.include_router(app.router)

@app.get("/health",status_code=200)
def healthcheck():
    logger.info('Health Check done')
    pass


@app.get("/")
def root():
    return "Begin Here" 


@app.get("/names",tags=['List of Id'])
def get_names(name: str, date: str):
    ids_r, names_r = get_data.get_ids(reviewer_name=name)
    ids__r=np.array(ids_r)
    ids___r=[]
    for i in ids__r:
        ids___r.append(int(i))
    #names__r=list(names_r)
    return {
        
        "ids":ids___r,
        "names":names_r
    
    }

models.Base.metadata.create_all(engine)