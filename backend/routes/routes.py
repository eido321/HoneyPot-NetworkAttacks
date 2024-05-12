from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..services import crud
from ..config import database, plaid


database.create_tables()

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Server is running"}

@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)