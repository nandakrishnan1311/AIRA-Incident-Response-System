from fastapi import FastAPI
from backend.schemas import LogRequest, LogResponse
from backend.model_loader import predict_log
from backend.incident_manager import create_incident

app = FastAPI(title="AIRA Backend")

@app.post("/predict", response_model=LogResponse)
def predict(request: LogRequest):
    result = predict_log(request.log_message)
    incident = create_incident(request.log_message, result["prediction"])

    if incident:
        print("INCIDENT CREATED:", incident)

    return result
