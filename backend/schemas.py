from pydantic import BaseModel

class LogRequest(BaseModel):
    log_message: str

class LogResponse(BaseModel):
    prediction: str
    score: float
