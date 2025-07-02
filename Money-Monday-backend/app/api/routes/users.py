from typing import Any, Annotated

from fastapi import APIRouter, Depends

from app.core.db import SessionDep
from app.models.user import User, UserCreate, UserRegister, UserPublic, UsersPublic
from app.api.deps import get_current_admin, get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", dependencies=[Depends(get_current_admin)], response_model=UsersPublic)
def read_users(session: SessionDep) -> Any:
    users = session.query(User).all()
    return UsersPublic(data=users, count=len(users))


@router.get("/{user_id}", dependencies=[Depends(get_current_admin)], response_model=UserPublic)
def read_user_by_id(user_id: int, session: SessionDep) -> Any:
    user = session.get(User, user_id)
    return user