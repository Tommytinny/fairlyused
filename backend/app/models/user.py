from sqlmodel import Field, Relationship
from app.models.base_model import BaseModel
from pydantic import EmailStr


class User(BaseModel, table=True):
    __tablename__ = "users"
    
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str
    hashed_password: str = Field(nullable=False)
    
    profile: "Profile" = Relationship(back_populates="user")
    
     