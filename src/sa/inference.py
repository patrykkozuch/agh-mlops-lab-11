import numpy as np
import onnxruntime as ort
from onnxruntime import InferenceSession
from tokenizers import Tokenizer

from sa.settings import Settings

SENTIMENT_MAP = {
    0: "negative",
    1: "neutral",
    2: "positive"
}


def load_classifier(settings: Settings):
    return ort.InferenceSession(settings.onnx_classifier_path)


def load_embedding_model(settings: Settings):
    return ort.InferenceSession(settings.onnx_embedding_model_path)


def load_tokenizer(settings: Settings):
    return Tokenizer.from_file(settings.tokenizer_dir + "/tokenizer.json")


def analyze_sentiment(
    sentence: str,
    tokenizer: Tokenizer,
    embedding_session: InferenceSession,
    classifier_session: InferenceSession
) -> str:
    # tokenize input
    encoded = tokenizer.encode(sentence)

    # prepare numpy arrays for ONNX
    input_ids = np.array([encoded.ids])
    attention_mask = np.array([encoded.attention_mask])

    # run embedding inference
    embedding_inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
    embeddings = embedding_session.run(None, embedding_inputs)[0]

    # run classifier inference
    classifier_input_name = classifier_session.get_inputs()[0].name
    classifier_inputs = {classifier_input_name: embeddings.astype(np.float32)}
    prediction = classifier_session.run(None, classifier_inputs)[0]

    return SENTIMENT_MAP.get(prediction[0], "unknown")  # return this label as response
