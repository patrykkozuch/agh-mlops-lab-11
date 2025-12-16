from fastapi import FastAPI

from sa.api.models.sa import PredictRequest, PredictResponse

from sa.inference import load_transformer, load_classifier, analyze_sentiment

app = FastAPI()

transformer = load_transformer()
clf = load_classifier()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction=analyze_sentiment(request.text, transformer, clf))

@app.get("/health")
def health_check():
    return {"status": "ok"}
