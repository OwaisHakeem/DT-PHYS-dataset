Step 5 — Full Multi Sensor Experiment Plan (e Health v2.0 + Arduino Uno) with Laptop as Aggregator
Context: Digital Twin + Federated Learning (Stress Prediction). Laptop replaces cloud layer.
Aim
Define a reproducible multi-sensor setup: sensor set, sampling strategy, unified dataset schema,
session protocol (baseline/task/recovery), and GitHub version-control procedure before Step 6.
Hardware and Sensors Available
• Arduino Uno (ATmega328P) + e Health Sensor Platform v2.0
• GSR (Galvanic Skin Response)
• ECG
• EMG
• Airflow (respiration)
• Temperature
• Pulse and oxygen functions (SpO / pulse)
• Body position detection (kit module)
• Laptop (central coordinator / aggregator)
Architecture Decision (Laptop as Cloud Replacement)
Edge: Arduino+eHealth captures signals (optionally Pi for local compute).
Laptop: storage + orchestration + (later) federated aggregation + twin registry.
Sampling Strategy (initial conservative rates)
• GSR: 5 Hz
• Temperature: 1 Hz
• SpO /Pulse: 1–2 Hz
• Airflow: 10–25 Hz (start low)
• ECG: 50–100 Hz (start low, increase if stable)
• EMG: 50–100 Hz (start low)
• Body position: 5–10 Hz
Unified CSV Schema (FL-friendly)
timestamp_ms,phase,label,gsr,ecg_raw,emg_raw,airflow_raw,spo2,pulse,temp_c,body_pos
phase: baseline | task | recovery
label: optional (e.g., self_report_0_10 or task_id)
Session Protocol (example)
1) Baseline: 2 min seated, normal breathing
2) Task: 2 min mental arithmetic OR paced breathing challenge
3) Recovery: 2 min seated rest
Record phase transition times or embed markers in stream
Sensor Integration Order (minimise troubleshooting)
• ECG → SpO /Pulse → Airflow → Temperature → EMG → Body position → Unified multi-sensor logger
GitHub Update Checklist (end of Step 5)
• Add docs/step-05-multisensor-plan.md
• Ensure docs/ehealth-library-procedure.md is present (library path + patches + verification)
• Optional: docs/data-schema.csv (header-only)
• Add arduino/step05_multisensor_scaffold/step05_multisensor_scaffold.ino
Commit message: Step 5: multi-sensor experiment plan and unified dataset schema
Safety/Data Governance (thesis note)
Do not publish identifiable personal data. Keep raw logs private; publish only anonymised/synthetic examples.