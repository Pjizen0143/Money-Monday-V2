from datetime import timedelta

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
# OAuth2PasswordRequestForm is a class dependency that declares a form body with The username, The password


from app.core.db import SessionDep
from app.core.config import settings
from app.core import security
from app.crud.user import authenticate
from app.models.utils import Token

router = APIRouter(tags=["login"])

@router.post("/login")
def login(session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate(session=session, username__or_email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=404, detail="Incorrect username/email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(access_token=security.create_access_token(user.user_id, expires_delta=access_token_expires))