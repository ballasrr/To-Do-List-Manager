# Это и есть корневой роут
from typing import Annotated
from app.schemas.users import CreateUser
from app.crud import crud
from fastapi import Path, APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def create_user(user: CreateUser):
    return crud.created_user(user=user)

