from pydantic import BaseModel

class Slot(BaseModel):
    id: int
    start_time: str
    end_time: str
    reserved: bool = False

class Booking(BaseModel):
    id: int
    start_time: str
    end_time: str
