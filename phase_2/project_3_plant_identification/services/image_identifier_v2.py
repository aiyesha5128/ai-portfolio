import os
import io
import requests
from dotenv import load_dotenv
from PIL import Image
load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
# For now we use a general model endpoint.
# Next, we will switch to a plant-specific model once you confirm output.
HF_MODEL_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}
def identify_plant(uploaded_file):
    """
    Sends the uploaded image to Hugging Face Inference API and returns:
    (predicted_label, confidence)
    """
    if not HF_API_TOKEN:
        return "unknown", 0.0
# Convert uploaded file to JPEG bytes
    image = Image.open(uploaded_file).convert("RGB")
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    img_bytes = buf.getvalue()
try:
        response = requests.post(
            HF_MODEL_URL,
            headers=HEADERS,
            data=img_bytes,
            timeout=60
        )
except requests.RequestException:
 return "unknown", 0.0
if response.status_code != 200:
 return "unknown", 0.0
preds = response.json()
# Expected format: [{"label": "...", "score": 0.8}, ...]
    if not isinstance(preds, list) or len(preds) == 0:
        return "unknown", 0.0
best = preds[0]
    label = best.get("label", "unknown")
    score = float(best.get("score", 0.0))
return label, round(score, 2)