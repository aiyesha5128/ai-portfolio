# 🏥 AI Medical Coding Assistant (ICD-10 + CPT)

## 📌 Overview
This project is a rule-based medical coding assistant that extracts ICD-10 diagnosis codes and CPT procedure codes from clinical notes.

It simulates basic clinical reasoning by identifying multiple conditions and procedures from a single note and returning structured coding outputs.

---

## 🚀 Current Version: Phase 1.5

### ✅ Features
- Multi-code detection (ICD-10 + CPT)
- Extracts multiple diagnosis codes from a single note
- Detects CPT codes for:
  - Evaluation & Management (E/M)
  - Imaging procedures (e.g., CT scans)
- Provides explanation ("reason") for each code
- Simple context-aware logic (not just keyword matching)
- Streamlit-based user interface

---

## 🧪 Examples

### Example 1 (Phase 1 behavior)

**Input:**
Patient is a new patient with dental caries.

**Output:**
- ICD-10: K02.9 — Dental caries  
- CPT: 99203 — New patient visit  

---

### Example 2 (Phase 1.5 behavior)

**Input:**
Patient is a new patient with chest pain and sinusitis. Evaluation and CT scan performed.

**Output:**

**ICD-10 Codes:**
- R07.9 — Chest pain, unspecified  
- J01.90 — Acute sinusitis  

**CPT Codes:**
- 99203 — New patient office visit  
- 71250 — CT chest without contrast  

---

## ⚠️ Current Limitations

- E/M levels (99202–99205) are estimated, not fully calculated
- Imaging codes may rely on limited context (body part not always explicitly validated)
- Not fully compliant with official ICD-10 / CPT coding guidelines
- Uses rule-based logic (no NLP/ML yet)

---

## 🛠️ Tech Stack

- Python
- Streamlit

---

## 📂 Project Structure
project_2_medical_coding/
│
├── app.py
├── data/
├── services/
└── utils/

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py


📈 Project Status

## Phase 1.5 Complete — Multi-code detection implemented 
🔧 Actively improving toward more accurate coding logic

🔄 Next Steps (Phase 2)
Improve E/M level selection using proper criteria
Add coding guidelines (ICD-10 & CPT rules)
Reduce assumption-based coding
Introduce NLP for better clinical understanding
Enhance procedure detection (beyond basic keywords)

💡 Goal

To evolve this project into a more realistic medical coding assistant that mimics real-world coding workflows and decision-making.