from fastapi import APIRouter

from app.api.routes import status, auth, profiles, listings

api_router = APIRouter()
api_router.include_router(status.router, prefix="/status")
api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(profiles.router, prefix="/profiles")
api_router.include_router(listings.router, prefix="/listings")