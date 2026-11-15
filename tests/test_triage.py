import pytest
from app import evaluate_triage

def test_emergency_chest_pain():
    result = evaluate_triage(["Chest Pain"], age=30, duration_days=1)
    assert result["level"] == "Emergency"

def test_moderate_symptoms():
    result = evaluate_triage(["Severe Abdominal Pain"], age=28, duration_days=2)
    assert result["level"] == "Moderate"

def test_elderly_risk_elevation():
    # Moderate symptom for age > 65 should escalate to Emergency
    result = evaluate_triage(["Severe Abdominal Pain"], age=72, duration_days=1)
    assert result["level"] == "Emergency"

def test_low_priority_symptom():
    result = evaluate_triage(["Persistent Cough"], age=22, duration_days=3)
    assert result["level"] == "Low"

def test_empty_symptoms():
    result = evaluate_triage([], age=25, duration_days=1)
    assert result["level"] == "None"
