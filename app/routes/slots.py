from fastapi import APIRouter
from app.database import slots
from app.models import Slot

router = APIRouter(prefix="/slots", tags=["Slots"])

@router.get("/", response_model=list[Slot])
def get_slots():
    return slots
