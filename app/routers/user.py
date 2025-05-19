from fastapi import APIRouter,status, Depends, HTTPException
from typing import List
from app.schemas import schemas
from app.models import models
from app.database.database import SessionDep
from app.core.hashing import Hash


router = APIRouter(
      prefix="/user",
    tags=["Users"]
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User,session: SessionDep):
    db_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, session: SessionDep):
    db_user = session.get(models.User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {user_id} not found"
        )
    return db_user
