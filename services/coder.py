import json

def load_codes(path):
    with open(path, "r") as f:
        return json.load(f)

icd_data = load_codes("data/icd10_codes.json")
cpt_data = load_codes("data/cpt_codes.json")


# ---------------- ICD ----------------
def find_icd(note):
    results = []
    note = note.lower()

    if any(word in note for word in ["caries", "tooth decay"]):
        results.append({
            "code": "K02.9",
            "description": "Dental caries, unspecified",
            "reason": "Keyword 'caries' matched"
        })

    # ✅ ADD THIS
    if "chest pain" in note:
        results.append({
            "code": "R07.9",
            "description": "Chest pain, unspecified",
            "reason": "Keyword 'chest pain' matched"
        })

    # ✅ ADD THIS
    if "sinusitis" in note:
        results.append({
            "code": "J01.90",
            "description": "Acute sinusitis, unspecified",
            "reason": "Keyword 'sinusitis' matched"
        })

    return results


# ---------------- PATIENT TYPE ----------------
def detect_patient_type(text):
    text = text.lower()

    if "new patient" in text:
        return "new"
    elif "established patient" in text:
        return "established"
    elif "follow up" in text:
        return "follow_up"

    return None


# ---------------- CONFLICTS ----------------
def detect_conflicts(note):
    note = note.lower()

    conflicts = []

    if "new patient" in note and "follow up" in note:
        conflicts.append("Conflicting terms: new patient + follow up")

    return conflicts


# ---------------- CPT ----------------
def find_cpt(text):
    results = []
    notetext = text.lower()

    # STEP 1: Imaging logic (CT scan, X-ray, MRI)
    if "ct scan" in text.lower():
        if "chest" in text.lower():
            results.append({
                "code": "71250",
                "description": "CT chest without contrast",
                "reason": "CT scan + chest pain context"
            })

                # STEP 2: E/M (Evaluation & Management)
    if "new patient" in text.lower() or "evaluation" in text.lower():
        results.append({
            "code": "99203",
            "description": "Office visit, new patient (moderate)",
            "reason": "New patient evaluation detected"
        })

    if any(word in text for word in ["new patient", "first visit"]):
        results.append({
            "code": "99203",
            "description": "Office visit, new patient",
            "reason": "New patient visit detected"
        })

    if any(word in text for word in ["follow up", "established", "revisit"]):
        results.append({
            "code": "99213",
            "description": "Office visit, established patient",
            "reason": "Follow-up visit detected"
        })

    # ✅ ADD THIS (important for your test case)
    if any(word in text for word in ["evaluation", "exam", "assessment"]):
        results.append({
            "code": "99213",
            "description": "Office visit (evaluation)",
            "reason": "Evaluation keyword matched"
        })

    return results


# ---------------- MAIN FUNCTION ----------------
def coder(text):
    icd_results = find_icd(text)
    cpt_results = find_cpt(text)
    conflicts = detect_conflicts(text)

    return {
        "ICD": icd_results,
        "CPT": cpt_results,
        "Warnings": conflicts
    }


# ---------------- OUTPUT DISPLAY (IMPORTANT PLACE) ----------------
def run(note):
    results = coder(note)

    print("\nResults")

    print("\nICD-10 Codes")
    for r in results["ICD"]:
        print(f"Code: {r['code']}")
        print(f"Description: {r['description']}")
        print(f"Reason: {r['reason']}\n")

    print("CPT Codes")
    for r in results["CPT"]:
        print(f"Code: {r['code']}")
        print(f"Description: {r['description']}")
        print(f"Reason: {r['reason']}\n")

    # ✅ ADD YOUR WARNING BLOCK HERE (CORRECT PLACE)
    if results.get("Warnings"):
        print("Warnings")
        for w in results["Warnings"]:
            print(f"⚠ {w}")