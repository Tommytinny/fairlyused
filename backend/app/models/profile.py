import uuid

from sqlmodel import Field, Relationship
from app.models.base_model import BaseModel


class Profile(BaseModel, table=True):
    __tablename__ = "profiles"
    
    user_id: uuid.UUID = Field(foreign_key="users.id", unique=True)
    display_name: str
    is_seller: bool = Field(default=False)
    is_verified: bool = Field(default=False)
    seller_rating: float | None = Field(default=None)
    
    user: "User" = Relationship(back_populates="profile")
    
     