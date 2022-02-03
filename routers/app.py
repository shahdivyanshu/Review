from turtle import st
from fastapi import APIRouter
router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.get("/names")
def get_names(name:str):
    pass
