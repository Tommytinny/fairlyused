import uuid
from sqlmodel import Session, select

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate


def get_profile(*, session: Session, user_id: uuid) -> Profile | None:
    statement = select(Profile).where(Profile.user_id == user_id)
    result = session.exec(statement).first()
    return result

def create_profile(*, session: Session, profile_create: ProfileCreate, owner_id: uuid) -> Profile:
    profile_data = profile_create.model_dump()
    db_obj = Profile(**profile_data, user_id=owner_id)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


    