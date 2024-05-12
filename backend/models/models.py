from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from config import database


class User(database.Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
