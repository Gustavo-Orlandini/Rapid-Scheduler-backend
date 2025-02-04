from fastapi import APIRouter, HTTPException
from app.models import Booking
from utils import load_slots, save_slots

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/")
async def create_booking(booking: Booking):
    slots = load_slots()
    for slot in slots:
        if slot.start_time == booking.start_time and slot.end_time == booking.end_time:
            if slot.reserved:
                raise HTTPException(status_code=400, detail="Slot already reserved.")
            slot.reserved = True
            save_slots(slots)
            return booking
    raise HTTPException(status_code=404, detail="Slot not found.")
