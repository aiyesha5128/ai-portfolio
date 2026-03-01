# 🌿 Project 3 — PlantPal v1.0 — Plant Identification Agent (MVP)

This project is part of **Phase 2** of my AI Engineering Portfolio.

---

## 📸 Demo

![PlantPal MVP](assets/demo.png)

---

## 🔎 Overview

PlantPal is a modular AI-ready houseplant identification assistant built using Streamlit.

This MVP demonstrates a complete AI workflow architecture:

- Image upload handling
- Prediction pipeline integration (`identify_plant()` service layer)
- Confidence score display
- Structured care instruction lookup from JSON
- Graceful fallback handling
- Clean modular separation (UI → Services → Data)

The focus of this version is **pipeline architecture and integration design**, preparing the system for real vision model integration.

---

## 🎯 MVP Capabilities

- Upload plant image
- Run prediction through a modular service layer
- Display predicted plant name with confidence score
- Retrieve plant care instructions from structured JSON database
- Manual plant selection via dropdown
- Error handling when predicted plant is not in care database

---

## 🛠 Tech Stack

- Python
- Streamlit (UI Layer)
- JSON-based structured plant database
- Modular architecture (UI → Services → Data)
- Environment-secured API configuration
- Git-based version control

---

## 🧠 Architecture Design

User Upload → Streamlit UI → identify_plant() →
Prediction Output → Care Lookup (JSON) → Display Results

This separation ensures:
- Clean scalability
- Easy model replacement
- Future AI model integration without UI changes

---

## 🚧 Current Status

✅ MVP Complete  
⚠️ Prediction component currently uses placeholder logic  
🚀 Vision-based plant classifier integration planned

---

## 🚀 Upcoming Enhancements (Next Iteration)

- Integrate pretrained plant image classification model
- Map scientific names to common plant names
- Improve prediction accuracy
- Add top-3 prediction output
- Expand local plant care database
- Deploy web-hosted version

---

## 🗂 Folder Structure


project_3_plantpal/
├── app/                # Streamlit UI
├── services/           # Prediction logic (v1 mock + v2 vision API)
│   ├── image_identifier_v1.py
│   └── image_identifier_v2.py
├── src/                # Care data handling
├── data/               # JSON plant database
├── assets/             # Demo images
├── requirements.txt
└── README.md

### Version Notes

- v1 → Mock prediction logic (randomized output)
- v2 → Hugging Face Vision model integration (API-based inference)

## 💡 Learning Outcome

This project focuses on building production-style AI architecture before optimizing model accuracy.

The goal is to design systems that are:
- Modular
- Scalable
- Replaceable
- Integration-ready

Model accuracy improvements are planned in the next version.