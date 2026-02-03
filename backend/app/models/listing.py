import uuid

from sqlmodel import Field, Relationship
from app.models.base_model import BaseModel


class Listing(BaseModel, table=True):
    __tablename__ = "listings"
    
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    price: float
    is_active: bool = Field(default=True)
    seller_id: uuid.UUID = Field(foreign_key="profiles.id")
    
    seller: "Profile" = Relationship()