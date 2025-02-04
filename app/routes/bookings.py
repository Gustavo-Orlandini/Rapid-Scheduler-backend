from fastapi import APIRouter, HTTPException
from app.database import bookings, slots
from app.models import Booking

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/")
async def create_booking(booking: Booking):
    for existing_booking in bookings:
        if existing_booking.start_time == booking.start_time and existing_booking.end_time == booking.end_time:
            raise HTTPException(status_code=400, detail="Slot já reservado.")

    bookings.append(booking)
    return booking
