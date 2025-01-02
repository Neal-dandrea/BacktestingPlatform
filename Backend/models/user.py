from sqlalchemy import Column, Integer, String
from ..database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

from .connection import Base, engine
from .models.user import User

Base.metadata.create_all(bind=engine)
