from app.models import Slot, Booking

slots = [
    Slot(id=1, start_time="2025-02-03T09:00:00", end_time="2025-02-04T10:00:00"),
    Slot(id=2, start_time="2025-02-04T14:00:00", end_time="2025-02-04T15:00:00"),
    Slot(id=3, start_time="2025-02-05T16:00:00", end_time="2025-02-05T17:00:00"),
    Slot(id=4, start_time="2025-02-06T11:00:00", end_time="2025-02-06T12:00:00"),
    Slot(id=5, start_time="2025-02-07T13:00:00", end_time="2025-02-7T14:00:00"),
]

bookings = []
