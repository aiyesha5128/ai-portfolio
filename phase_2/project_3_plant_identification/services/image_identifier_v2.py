import os
import io
import requests
from dotenv import load_dotenv
from PIL import Image
load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL_URL = HF_MODEL_URL = HF_MODEL_URL = "https://router.huggingface.co/hf-inference/models/nateraw/vit-base-beans"
HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "image/jpeg"
}
def normalize_label(label):
    label = label.lower()

    # 🚫 Remove disease-specific outputs
    if any(x in label for x in ["rust", "spot", "blight", "mold"]):
        return "houseplant"

    if label == "healthy":
        return "houseplant"

    if "bean" in label:
        return "plant"

    return label

def identify_plant(uploaded_file):
    if not HF_API_TOKEN:
        return "unknown", 0.0
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
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
    except requests.RequestException as e:
        print("API ERROR:", e)
        return "unknown", 0.0
    if response.status_code != 200:
        return "unknown", 0.0
    preds = response.json()
    if not isinstance(preds, list) or len(preds) == 0:
        return "unknown", 0.0
    best = preds[0]
    label = best.get("label", "unknown")
    score = float(best.get("score", 0.0))

    
    label = normalize_label(label)

    # 🚀 Normalize output
    if any(x in label for x in ["rust", "spot", "disease"]):
        label = "plant"
    elif label == "healthy":
        label = "plant"

    return label, round(score, 2)