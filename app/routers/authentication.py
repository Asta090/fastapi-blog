from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, models, token
from fastapi.security import OAuth2PasswordRequestForm
from ..database import SessionDep
from ..hashing import Hash


router=APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post("/",response_model=schemas.Token)
async def login(
    session: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = session.query(models.User).filter(models.User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
    if not Hash.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password"
        )
    
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
