from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError
from . import token
from app.models import models
from app.database import database
from app.schemas import schemas


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    current_token: str = Depends(oauth2_scheme),
    session: database.SessionDep = None
):
  credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
  )
  return token.verify_token(current_token, credentials_exception)
