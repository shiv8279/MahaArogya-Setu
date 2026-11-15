# MahaArogya Setu

Healthcare triage web application developed for **Smart India Hackathon (SIH 2026)**.

MahaArogya Setu assists users in evaluating symptoms across 40+ common and acute health conditions, providing preliminary triage assessment, suggested home care / urgency level, and recommendations for nearby medical centers.

---

## Features

- **Rule-Based Triage Logic:** Evaluates severity indicators to classify symptoms into low, moderate, or urgent medical emergencies.
- **Fast Response Times:** Built with Streamlit and lightweight data structures to maintain low latency even on mobile networks.
- **Comprehensive Test Coverage:** Includes 170+ unit and functional test cases verifying edge cases, boundary inputs, and input validation.
- **Clinic & Hospital Guidance:** Maps triage outcomes to appropriate levels of care (primary clinic vs. emergency ward).

---

## Tech Stack

- **Backend & Logic:** Python 3.9+
- **Frontend / UI:** Streamlit
- **Testing:** PyTest (Functional, Regression, and Boundary Value Testing)
- **Data & Storage:** Lightweight JSON / Python dictionaries for rapid in-memory lookups

---

## Local Setup

### Prerequisites
- Python 3.9 or higher installed

### Installation

1. Clone this repository:
```bash
git clone https://github.com/shiv8279/MahaArogya-Setu.git
cd MahaArogya-Setu
```

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install streamlit pytest
```

4. Run the web application:
```bash
streamlit run app.py
```

---

## Testing & Quality Assurance

To execute the automated test suite:
```bash
pytest tests/ -v
```

The test suite covers:
- Boundary condition checks for user age and symptom severity ratings
- Invalid input handling and fallback messaging
- Triage classification consistency across all 40+ supported symptom pathways

---

## Team & Contribution

- **Shiv Upadhyay** — Project Lead & QA Coordinator (B.Tech CSE - AI, Galgotias University)
- Developed as an official project for **Smart India Hackathon 2026**.
