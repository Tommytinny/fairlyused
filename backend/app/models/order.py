import uuid

from sqlmodel import Field, Relationship
from app.models.base_model import BaseModel

class OrderStatus(str, Enum):
    PENDING = "pending"        # buyer placed order
    PAID = "paid"              # escrow funded (future)
    COMPLETED = "completed"    # seller fulfilled
    CANCELLED = "cancelled"    # buyer/seller cancelled

class Order(BaseModel, table=True):
    __tablename__ = "orders"
    
    buyer_id: int = Field(foreign_key="profiles.id")
    listing_id: int = Field(foreign_key="listings.id", unique=True)

    amount: float
    status: OrderStatus = Field(default=OrderStatus.PENDING)

    buyer: "Profile" = Relationship()
    listing: "Listing" = Relationship()