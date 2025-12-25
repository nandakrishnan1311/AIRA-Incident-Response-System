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

## 🚀 Phase 3 – Dockerized Deployment (Completed ✅)

This phase focuses on containerizing the FastAPI-based ML inference backend using Docker to ensure consistent and production-ready deployment.

---

### 🐳 Build Docker Image

From the project root directory, build the Docker image:

```bash
docker build -t aira-backend .
```
### Expected output:

```bash
Successfully built <image_id>
Successfully tagged aira-backend
```


⚠️ Note: The first build may take some time as dependencies are installed. This is normal.

### ▶️ Run Docker Container

Run the Docker container using the built image:

```bash
docker run -p 8000:8000 aira-backend
```

Expected logs:

```bash
Uvicorn running on http://0.0.0.0:8000
Application startup complete.
```

This confirms that the FastAPI backend and the trained ML model are running successfully inside the Docker container.

### 🌐 Test the API in Browser (Very Important)

Open your web browser and navigate to:

```bash
http://127.0.0.1:8000/docs
```

This opens the Swagger UI, which allows interactive testing of the API endpoints.

### Screenshorts

![alt text](<screenshots/Screenshot (453).png>)

![alt text](<screenshots/Screenshot (454).png>)