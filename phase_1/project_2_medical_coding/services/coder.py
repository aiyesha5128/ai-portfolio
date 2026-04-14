import json

def load_codes(path):
    with open(path, "r") as f:
        return json.load(f)

icd_data = load_codes("data/icd10_codes.json")
cpt_data = load_codes("data/cpt_codes.json")

def find_icd(text):
    text = text.lower()
    for keyword, value in icd_data.items():
        if keyword in text:
            return {
                "code": value["code"],
                "description": value["description"],
                "reason": f"Keyword '{keyword}' matched"
            }
    return None

def find_cpt(text):
    text = text.lower()
    for keyword, value in cpt_data.items():
        if keyword in text:
            return {
                "code": value["code"],
                "description": value["description"],
                "reason": f"Keyword '{keyword}' matched"
            }
    return None