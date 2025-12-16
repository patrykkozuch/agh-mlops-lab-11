from unittest import TestCase
from pydantic import ValidationError

from sa.api.models.sa import PredictRequest


class TestPredictRequest(TestCase):
    def test_text_field__empty(self):
        with self.assertRaises(ValidationError):
            PredictRequest(text="")

    def test_text_field(self):
        request = PredictRequest(text="Analyse this")
        assert request.text == "Analyse this"
