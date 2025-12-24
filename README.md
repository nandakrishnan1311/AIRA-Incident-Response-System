# AIRA – AI Incident Response & Root Cause Analysis System

AIRA is an AI-powered system that detects anomalous system logs and creates incidents automatically using machine learning.

## Phase 1 – Log Anomaly Detection
- Trained Isolation Forest on simulated system logs
- Used TF-IDF for log vectorization
- Unsupervised anomaly detection
- Model trained in Google Colab and versioned using GitHub

## Tech Stack
- Python
- Scikit-learn
- FastAPI (upcoming)
- React (upcoming)

## Project Structure

### ML Details
- Algorithm: Isolation Forest
- Input: Raw system log messages
- Output: NORMAL / ANOMALY classification

---

## 🔹 Phase 2 – Backend ML Inference API (Completed ✅)

### What was built
- Production-style **FastAPI backend**
- Loaded trained ML model (`.pkl`) at application startup
- REST API endpoint for real-time log anomaly detection
- Automatic incident triggering for anomalous logs
- Interactive API testing using **Swagger UI**

### API Endpoint

### Screenshorts

![alt text](<screenshots/Screenshot%20(443).png>)

![alt text](<screenshots/Screenshot%20(444).png>)

![alt text](<screenshots/Screenshot%20(445).png>)

![alt text](<screenshots/Screenshot%20(446).png>)

![alt text](<screenshots/Screenshot%20(447).png>)