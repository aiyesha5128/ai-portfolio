import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


load_dotenv()
# Get your Hugging Face API token
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
print("TOKEN:", HF_TOKEN)  # debug

client = InferenceClient(token=HF_TOKEN)
def identify_plant(image_file):
    try:
        image_file.seek(0)
        image_bytes = image_file.read()

        print("TOKEN:", HF_TOKEN)



        results = client.image_classification(
            image_bytes,
            model="microsoft/resnet-50"  # public, works without gating
        )

        print("HF RAW RESULT:", results)

        if not results:
            return []

        predictions = [
            {'name': r['label'], 'score': r['score']}
            for r in results
        ]

        return predictions

    except Exception as e:
        print("ERROR:", e)
        return []