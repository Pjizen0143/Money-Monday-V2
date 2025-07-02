from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from app.core.config import settings
from app.core.db import SessionDep, SessionLocal
from app.models import User

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_BETA_STR}/login"
)

TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_current_user(session: SessionDep, token: TokenDep) -> User:
    try:
        payload = jwt.decode(
            token, "KEY", algorithms=["HS256"]
        )
        user_id = payload.get("user_id")
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_current_admin(current_user: CurrentUser) -> User:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
