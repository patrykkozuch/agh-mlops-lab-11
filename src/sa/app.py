from fastapi import FastAPI

from sa.api.models.sa import PredictRequest, PredictResponse

from sa.inference import analyze_sentiment, load_tokenizer, load_embedding_model, load_classifier
from sa.settings import Settings

app = FastAPI()
settings = Settings()

tokenizer = load_tokenizer(settings)
embedding_session = load_embedding_model(settings)
clf_session = load_classifier(settings)


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(
        prediction=analyze_sentiment(
            sentence=request.text,
            tokenizer=tokenizer,
            embedding_session=embedding_session,
            classifier_session=clf_session
        )
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}
