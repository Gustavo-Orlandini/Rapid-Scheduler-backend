from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

from app.routes import bookings, slots

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "production")
DEBUG = os.getenv("DEBUG", "false")

app = FastAPI(debug=(DEBUG.lower() == "true"))

origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)

app.include_router(slots.router)
app.include_router(bookings.router)

@app.get("/")
def read_root():
    return {"message": f"App is running in {APP_ENV} mode."}
