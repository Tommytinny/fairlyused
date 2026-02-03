from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated, Any
from datetime import timedelta

from app.api.deps import CurrentUser, SessionDep
from app.core.security import create_access_token
from app.core.config import get_settings
from app.schemas.user import UserPublic, UserCreate
from app.schemas.auth import Token
from app.services.auth import authenticate_user, create_user


settings = get_settings()
router = APIRouter(tags=["auth"])


@router.post("/signup", response_model=UserPublic)
def signup(session: SessionDep, user_in: UserCreate) -> Any:
    user = create_user(
        session=session, user_create=user_in
    )
    return user


@router.post("/login")
def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Token:
    user = authenticate_user(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )
    
@router.get("/me", response_model=UserPublic)
def get_me(current_user: CurrentUser) -> Any:
    return current_user