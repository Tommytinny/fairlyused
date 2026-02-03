from fastapi import APIRouter


router = APIRouter(tags=["status"])


@router.get("/")
def get_status():
    return {
        "status": "ok"
    }