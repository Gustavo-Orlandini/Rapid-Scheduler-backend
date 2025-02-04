from fastapi import APIRouter

from utils import load_slots

router = APIRouter(prefix="/slots", tags=["Slots"])

@router.get("/")
async def get_slots():
    return load_slots()