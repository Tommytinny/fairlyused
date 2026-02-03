import uuid

from sqlmodel import Field, SQLModel


class ProfileBase(SQLModel):
    display_name: str = Field(unique=True)
    is_seller: bool = False
    is_verified: bool = False
    is_seller: float | None = None
    

class ProfileCreate(ProfileBase):
    pass


class ProfilePublic(ProfileBase):
    id: uuid.UUID
    

class ProfilesPublic(SQLModel):
    data: list[ProfilePublic]
    count: int