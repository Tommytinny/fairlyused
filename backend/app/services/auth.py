from sqlmodel import Session, select

from app.models.user import User
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate

def create_user(*, session: Session, user_create: UserCreate) -> User:
    user_data = user_create.model_dump(exclude={"password"})
    hashed = hash_password(user_create.password)
    
    db_obj = User(**user_data, hashed_password=hashed)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first()
    return session_user

def authenticate_user(*, session: Session, email: str, password: str) -> User | None:
    db_user = get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user

