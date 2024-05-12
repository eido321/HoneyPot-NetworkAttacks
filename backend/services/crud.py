from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, Request
from uuid import UUID

from schemas import schemas
from models import models

import os
from dotenv import load_dotenv

load_dotenv()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, email=user.email, hashed_password=utils.hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
