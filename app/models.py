from pydantic import BaseModel

class Slot(BaseModel):
    id: int
    start_time: str  
    end_time: str    

class Booking(BaseModel):
    id: int
    start_time: str  
    end_time: str 
