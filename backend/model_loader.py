import joblib

MODEL_PATH = "backend/models/isolation_forest_model.pkl"
VECTORIZER_PATH = "backend/models/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_log(log_message: str):
    X = vectorizer.transform([log_message])
    prediction = model.predict(X)[0]
    score = model.decision_function(X)[0]

    return {
        "prediction": "ANOMALY" if prediction == -1 else "NORMAL",
        "score": float(score)
    }
