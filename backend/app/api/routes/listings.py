import uuid

from fastapi import APIRouter, HTTPException

from app.api.deps import CurrentUser, SessionDep
from app.core.config import get_settings
from app.schemas.listing import ListingCreate, ListingOut, ListingUpdate
from app.services.profile import get_profile
from app.services.listing import (
    get_listing,
    get_listings,
    create_listing,
    update_listing,
    delete_listing
)


settings = get_settings()
router = APIRouter(tags=["listings"])


@router.post("/", response_model=ListingOut)
def create_listing_route(session: SessionDep, current_user: CurrentUser, listing_in: ListingCreate):
    profile = get_profile(session=session, user_id=current_user.id)
    if not profile or not profile.is_seller:
        raise HTTPException(status_code=403, detail="Seller access required")
    
    new_listing = create_listing(session=session, current_user=current_user, listing_in=listing_in)
    
    return new_listing

@router.get("/", response_model=list[ListingOut])
def list_listings(session: SessionDep):
    all_listing = get_listings(session=session)
    return all_listing

@router.get("/{listing_id}", response_model=ListingOut)
def get_single_listing(session: SessionDep, listing_id: uuid):
    listing = get_listing(session=session, listing_id=listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

@router.put("/{listing_id}", response_model=ListingOut)
def update_my_listing(
    session: SessionDep,
    listing_id: uuid,
    listing_update: ListingUpdate,
    current_user: CurrentUser
):
    listing = get_listing(session=session, listing_id=listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    profile = get_profile(session=session, user_id=current_user.id)
    if listing.seller_id != profile.id:
        raise HTTPException(status_code=403, detail="Not your listing")

    return update_listing(session=session, listing=listing, listing_in=listing_update)

@router.delete("/{listing_id}")
def delete_my_listing(
    session: SessionDep,
    listing_id: uuid,
    current_user: CurrentUser,
):
    listing = get_listing(session=session, listing_id=listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    profile = get_profile(session=session, user_id=current_user.id)
    if listing.seller_id != profile.id:
        raise HTTPException(status_code=403, detail="Not your listing")

    delete_listing(session=session, listing=listing)
    return {"detail": "Listing deleted"}