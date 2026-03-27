def generate_care_guide(plant_name):
    if plant_name == "unknown":
        return "No care guide available."

    return f"""
### 🌿 Plant Care Guide for {plant_name}

**Light:**  
Bright indirect sunlight  

**Water:**  
Water once per week. Allow soil to dry slightly  

**Humidity:**  
Moderate humidity preferred  

**Temperature:**  
18–30°C  

**Tip:**  
Avoid overwatering to prevent root rot  
"""