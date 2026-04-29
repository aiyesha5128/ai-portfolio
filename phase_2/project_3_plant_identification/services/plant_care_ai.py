CARE_GUIDES = {
    "Ficus lyrata": "Water once a week, indirect sunlight, keep soil moist but not soggy.",
    "Monstera deliciosa": "Water when top soil is dry, bright indirect light, moderate humidity.",
    "Epipremnum aureum": "Low maintenance, water when soil is dry, can tolerate low light.",
     "Money Plant": "Water every 3–5 days, indirect sunlight, can grow in water or soil."
}

def get_care_guide(plant_name):
    """
    Return care guide text for a given plant name.
    """
    return CARE_GUIDES.get(plant_name, "Care guide not available for this plant.")