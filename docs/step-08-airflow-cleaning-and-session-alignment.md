# Step 8 — Airflow Cleaning and Session Alignment (Session 01)

## Goal
Convert raw Airflow sensor phase recordings into a single, continuous, **WESAD-inspired** session file with explicit phase labels and **dual timestamps**, suitable for later multi-sensor fusion, Digital Twin state updates, and Federated Learning pipelines.

This session follows a controlled protocol:
**3 min relax → 3 min stairs → 3 min recovery**

Phase timing is recorded in:
- `data/airflow/session01/airflow_session01_notes.txt`

---

## Inputs (Session 01)

Raw phase files:
- `data/airflow/session01/airflow_raw_20251230_session01_relax.csv`
- `data/airflow/session01/airflow_raw_20251230_session01_stairs.csv`
- `data/airflow/session01/airflow_raw_20251230_session01_recovery.csv`

Labeled merge (created before cleaning):
- `data/airflow/session01/airflow_session01_labeled.csv`

---

## Processing Script
Cleaning + alignment is performed using:
- `scripts/clean_airflow_session01.py`

Run:
```bash
python scripts/clean_airflow_session01.py
