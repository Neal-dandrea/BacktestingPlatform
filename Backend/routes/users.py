from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..models.user import User

router = APIRouter()

@router.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email, hashed_password="hashed_pw")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
