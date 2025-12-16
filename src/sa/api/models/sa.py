from pydantic import BaseModel, validator, field_validator


class PredictRequest(BaseModel):
    text: str

    @field_validator('text')
    @classmethod
    def text_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Text cannot be empty')
        return v


class PredictResponse(BaseModel):
    prediction: str
