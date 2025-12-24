import uuid
from datetime import datetime

def create_incident(log_message, prediction):
    if prediction == "ANOMALY":
        return {
            "incident_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow(),
            "log": log_message,
            "severity": "HIGH"
        }
    return None
