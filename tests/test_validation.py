import pytest
from app import evaluate_triage
def test_low(): assert evaluate_triage(["Mild Headache"], 25, 1)["level"] == "Low"
