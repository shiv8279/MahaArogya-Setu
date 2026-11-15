import streamlit as st
from datetime import datetime

st.set_page_config(page_title="MahaArogya Setu", page_icon="🏥", layout="wide")

st.title("🏥 MahaArogya Setu — Healthcare Triage Platform")
st.caption("Smart India Hackathon (SIH 2026) Submission | Developed by Shiv Upadhyay & Team")

# Triage Knowledge Base
TRIAGE_RULES = {
    "Chest Pain": {"severity": "Emergency", "action": "Immediate Hospitalization / Call 108", "care": "Do not exert yourself. Keep calm."},
    "Shortness of Breath": {"severity": "Emergency", "action": "Urgent Medical Attention Required", "care": "Sit upright, avoid tight clothing."},
    "High Fever (>102°F)": {"severity": "Moderate", "action": "Visit Primary Care Clinic within 24h", "care": "Hydrate with electrolytes, paracetamol if prescribed."},
    "Persistent Cough": {"severity": "Low", "action": "Teleconsultation or OPD visit", "care": "Warm fluids, steam inhalation, rest."},
    "Mild Headache": {"severity": "Low", "action": "Home Monitoring & Rest", "care": "Drink water, reduce screen time."},
    "Severe Abdominal Pain": {"severity": "Moderate", "action": "Clinical Ultrasound / Urgent OPD", "care": "Avoid solid foods, seek doctor review."},
    "Dizziness / Fainting": {"severity": "Moderate", "action": "Doctor Consultation & Blood Pressure Check", "care": "Lie flat with legs elevated."}
}

def evaluate_triage(selected_symptoms, age, duration_days):
    if not selected_symptoms:
        return {"level": "None", "message": "Please select at least one symptom."}
    
    max_level = "Low"
    actions = []
    
    for s in selected_symptoms:
        rule = TRIAGE_RULES.get(s, {"severity": "Low", "action": "Consult local practitioner", "care": "Rest"})
        if rule["severity"] == "Emergency":
            max_level = "Emergency"
        elif rule["severity"] == "Moderate" and max_level != "Emergency":
            max_level = "Moderate"
        actions.append(f"{s}: {rule['action']} ({rule['care']})")
        
    if age > 65 and max_level == "Moderate":
        max_level = "Emergency"
        actions.append("Elevated risk due to age factor (>65 years).")
        
    return {"level": max_level, "details": actions}

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Patient Symptoms & Vitals")
    age = st.number_input("Patient Age", min_value=1, max_value=120, value=25)
    duration = st.slider("Symptom Duration (Days)", 1, 30, 2)
    symptoms = st.multiselect(
        "Select Observed Symptoms",
        options=list(TRIAGE_RULES.keys()),
        default=["Persistent Cough"]
    )
    evaluate_btn = st.button("Evaluate Triage Priority", type="primary")

with col2:
    st.subheader("Triage Recommendation")
    if evaluate_btn:
        result = evaluate_triage(symptoms, age, duration)
        level = result["level"]
        
        if level == "Emergency":
            st.error("🚨 PRIORITY: EMERGENCY MEDICAL ESCALATION")
            st.write("**Recommended Route:** Call emergency services (108) or proceed immediately to nearest trauma/emergency department.")
        elif level == "Moderate":
            st.warning("⚠️ PRIORITY: MODERATE — URGENT CLINICAL REVIEW")
            st.write("**Recommended Route:** Visit primary healthcare centre / OPD within 24 hours.")
        else:
            st.success("✅ PRIORITY: LOW / HOME CARE")
            st.write("**Recommended Route:** Standard home care, rest, and routine teleconsultation if symptoms persist.")
            
        st.markdown("#### Triage Guidance Summary")
        for item in result["details"]:
            st.write(f"• {item}")
