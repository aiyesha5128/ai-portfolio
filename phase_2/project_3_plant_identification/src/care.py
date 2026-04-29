import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "plant_care.json"

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_care(plant_name: str):
    data = load_data()
    return data.get(plant_name)

def get_plant_names():
    data = load_data()
    return sorted(list(data.keys()))

