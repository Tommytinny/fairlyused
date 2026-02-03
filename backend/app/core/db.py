from sqlmodel import SQLModel, Session, create_engine
from app.core.config import get_settings


settings = get_settings()
engine = create_engine(settings.sqlalchemy_database_uri.unicode_string())

"""def init_db(session: Session) -> None:
    # create all tables for models
    #SQLModel.metadata.create_all(engine)
    
    user = session.exec(
        select(User).where(User.email == settings.SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)"""