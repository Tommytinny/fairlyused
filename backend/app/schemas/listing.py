from sqlmodel import Field, SQLModel


class ListingBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    price: float

class ListingCreate(ListingBase):
    pass

class ListingUpdate(ListingBase):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    is_active: bool | None = None

class ListingOut(ListingBase):
    id: int
    is_active: bool
    seller_id: int

