import json
from typing import List

from app.models import Slot

SLOTS_FILE = "./slots.json"

def load_slots() -> List[Slot]:
    try:
        with open(SLOTS_FILE, "r") as file:
            slots_data = json.load(file)
        return [Slot(**slot) for slot in slots_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Error decoding the JSON file: {e}")

def save_slots(slots: List[Slot]) -> None:
    try:
        with open(SLOTS_FILE, "w") as file:
            json.dump([slot.model_dump() for slot in slots], file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error saving slots to the JSON file: {e}")
