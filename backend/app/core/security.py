import jwt
from passlib.context import CryptContext

from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.config import get_settings


settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = settings.SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # 1 hour


# password hashing
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hash_password: str) -> bool:
    return pwd_context.verify(password, hash_password)

# JWT token
def create_access_token(subject: str, expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[settings.ALGORITHM])
    