from fastapi import APIRouter, HTTPException

from app.api.deps import CurrentUser, SessionDep
from app.core.config import get_settings
from app.schemas.profile import ProfileCreate, ProfilePublic, ProfilesPublic
from app.services.profile import get_profile, create_profile


settings = get_settings()
router = APIRouter(tags=["profiles"])


@router.post("/me", response_model=ProfilePublic)
def create_my_profile(session: SessionDep, current_user: CurrentUser, data: ProfileCreate):
    existing = get_profile(session=session, user_id=current_user.id)
    if existing:
        raise HTTPException(status_code=400, detail="Profile already exists")
    
    new_profile = create_profile(session=session, profile_create=data, owner_id=current_user.id)
    return new_profile

@router.get("/me", response_model=ProfilePublic)
def get_my_profile(session: SessionDep, current_user: CurrentUser):
    profile = get_profile(session=session, user_id=current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile