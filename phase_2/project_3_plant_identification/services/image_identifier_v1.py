import random
def identify_plant(image_file):
    # Temporary mock AI logic
    plant_options = ["Pothos", "Snake Plant", "Aloe Vera"]
    predicted = random.choice(plant_options)
    confidence = round(random.uniform(0.6, 0.95), 2)
    
    return predicted, confidence
