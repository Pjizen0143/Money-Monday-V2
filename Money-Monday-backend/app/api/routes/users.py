from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app.core.db import SessionDep
from app.models.user import User, UserCreate, UserRegister, UserPublic, UsersPublic
from app.api.deps import get_current_admin, CurrentUser
from app.models.common import Message
from app.crud import user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/signup", response_model=UserPublic)
def register_user(user_in: UserRegister, session: SessionDep) -> Any:
    new_user = user.get_user_by_username(session=session, username=user_in.username)
    if new_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = user.get_user_by_email(session=session, email=user_in.email)  # type: ignore
    if new_user:
        raise HTTPException(status_code=400, detail="email already exists")

    new_user = UserCreate.model_validate(user_in)
    new_user = user.create_user(session=session, user_create=new_user)
    return new_user


@router.delete("/{user_id}", dependencies=[Depends(get_current_admin)])
def delete_user(user_id: int, session: SessionDep, current_user: CurrentUser) -> Message:
    user_target = session.get(User, user_id)
    if not user_target:
        raise HTTPException(status_code=404, detail="User not found")
    if user_target == current_user:
        raise HTTPException(status_code=403, detail="admin are not allowed to delete themselves")

    return user.delete_user(session=session, user=user_target)


@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> Any:
    return current_user


# -------- API endpoint for Admin only --------
@router.get("/", dependencies=[Depends(get_current_admin)], response_model=UsersPublic)
def read_users(session: SessionDep) -> Any:
    users = session.query(User).all()
    return UsersPublic(data=users, count=len(users))


@router.get("/{user_id}", dependencies=[Depends(get_current_admin)], response_model=UserPublic)
def read_user_by_id(user_id: int, session: SessionDep) -> Any:
    user_data = session.get(User, user_id)
    return user_data


@router.post("/", dependencies=[Depends(get_current_admin)], response_model=UserPublic)
def create_user(user_in: UserCreate, session: SessionDep) -> Any:
    new_user = user.get_user_by_username(session=session, username=user_in.username)
    if new_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = user.get_user_by_email(session=session, email=user_in.email) # type: ignore
    if new_user:
        raise HTTPException(status_code=400, detail="email already exists")

    new_user = user.create_user(session=session, user_create=user_in)
    return new_user

# -------- API endpoint for Admin only --------
