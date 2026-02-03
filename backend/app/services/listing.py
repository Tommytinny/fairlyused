import uuid
from sqlmodel import Session, select

from app.models.listing import Listing
from app.schemas.listing import ListingCreate, ListingUpdate

def create_listing(
    *,
    session: Session, 
    seller_id: uuid, 
    listing_in: ListingCreate
) -> Listing:
    listing = Listing(
        seller_id=seller_id,
        **listing_in.dict()
    )
    session.add(listing)
    session.commit()
    session.refresh(listing)
    return listing

def get_listing(*, session: Session, listing_id: uuid) -> Listing | None:
    statement = select(Listing).where(Listing.id == listing_id)
    result = session.exec(statement).first()
    return result

def get_listings(*, session: Session):
    statement = select(Listing).where(Listing.is_active == True)
    result = session.exec(statement).all()
    return result

def update_listing(
    *,
    session: Session,
    listing: Listing,
    listing_in: ListingUpdate
) -> Listing:
    update_dict = listing_in.model_dump(exclude_unset=True)
    listing.sqlmodel_update(update_dict)
    session.add(listing)
    session.commit()
    session.refresh(listing)
    return listing

def delete_listing(*, session: Session, listing: Listing):
    session.delete(listing)
    session.commit()
