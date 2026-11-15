import pytest
from app import evaluate_triage
def test_age(): assert evaluate_triage(["High Fever (>102°F)"], 70, 1)["level"] == "Emergency"
