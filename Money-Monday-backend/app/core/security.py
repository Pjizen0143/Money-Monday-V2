from datetime import datetime, timedelta, timezone
from typing import Any
# timedelta คือชนิดข้อมูลใน datetime ที่เก็บระยะเวลาเอาไว้ เช่น 2 ชั่วโมง

import jwt

from passlib.context import CryptContext

from app.core.config import Settings

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(payload, Settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
