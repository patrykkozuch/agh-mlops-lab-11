from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    S3_BUCKET_NAME: str = ""
    MODELS_PATH: str = "models/"
    ARTIFACTS_PATH: str = "artifacts/"

    models_zip_path: str = ARTIFACTS_PATH + "models.zip"
    classifier_joblib_path: str = ARTIFACTS_PATH + "classifier.joblib"
    sentence_transformer_dir: str = ARTIFACTS_PATH + "sentence_transformer.model"

    embedding_dim: int = 384

    onnx_classifier_path: str = MODELS_PATH + "classifier.onnx"
    tokenizer_dir: str = MODELS_PATH + "tokenizer"
    onnx_embedding_model_path: str = MODELS_PATH + "embedding_model.onnx"
