from pydantic import EmailStr

from sqlmodel import SQLModel, Field

# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, nullable=False, index=True, max_length=255)
    is_admin: bool = False
    username: str = Field(unique=True, nullable=False, max_length=32)


# Properties to receive via API on creation
class UserCreate(UserBase):
    # สำหรับสร้าง User
    password: str = Field(min_length=8, max_length=32)


class UserRegister(SQLModel):
    # สำหรับรับข้อมูลจาก User
    email: EmailStr = Field(max_length=255)
    username: str = Field(max_length=32)
    password: str = Field(min_length=8, max_length=32)


# Properties to receive via API on update, all are optional
class UserUpdateMe(SQLModel):
    email: EmailStr | None = Field(max_length=255)
    username: str | None = Field(max_length=32)


class UserUpdatePassword(SQLModel):
    current_password: str | None = Field(max_length=32)
    new_password: str | None = Field(max_length=32)


# database model
class User(UserBase, table=True):
    user_id: int = Field(default=None, nullable=False, index=True, primary_key=True)
    hashed_password: str

# Properties to return via API, id is always required
class UserPublic(UserBase):
    user_id: int


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int
