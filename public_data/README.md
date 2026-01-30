# Public Dataset (Processed)

This folder contains the processed (cleaned and time-aligned) datasets used for Digital Twin (Eclipse Ditto) and Federated Learning experiments.

## Session Protocol
Each recording session follows a 9-minute (3–3–3) protocol:
- Relax: 3 minutes
- Stairs (physical stress): 3 minutes
- Recovery: 3 minutes

Target aligned timeline: 0–540,000 ms.

## Files
All files below are from Session 01 and are processed outputs:

- `session01/gsr_session01_clean.csv` — Galvanic Skin Response (EDA)
- `session01/ecg_session01_clean.csv` — ECG waveform (cleaned)
- `session01/airflow_session01_clean.csv` — Airflow/respiration amplitude signal
- `session01/session01_multisensor_clean.csv` — Fused multisensor dataset (outer join, NaNs preserved)

## Columns (typical)
Common columns may include:
- `session_timestamp_ms` — aligned session timeline
- `timestamp_ms` — device-local timestamp
- `phase` — relax / stairs / recovery
- sensor-specific fields (e.g., `gsr_raw`, `ecg_raw`, `airflow_raw`)

## Notes on Processing
- Processed datasets are provided for reproducible research and experimentation.
- Raw acquisition files, notes, and intermediate artifacts remain private in `data/` and are not published.
- No interpolation has been applied at this stage (raw-first principle).

## Intended Use and Ethics
This dataset is provided for research/educational use and is **non-diagnostic**. It must not be used for clinical decision-making.
