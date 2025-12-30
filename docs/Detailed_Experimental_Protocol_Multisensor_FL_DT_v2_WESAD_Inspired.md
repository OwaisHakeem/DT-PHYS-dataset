Detailed Experimental Protocol for Multisensor Data

Acquisition and Communication Overhead

Measurement (WESAD-Inspired Session Design)

This document presents a revised and extended experimental protocol for multisensor physiological data

acquisition and communication overhead evaluation within a Federated Learning–Digital Twin (FL–DT)

framework. The protocol incorporates a WESAD-inspired session structure while maintaining a simplified,

reproducible design suitable for system-level validation.

1. Experimental Role within the FL–DT Framework

The experiment functions as a real-world healthcare case study complementing simulation-based

evaluations. Physiological signals populate and update a human-centric Digital Twin, while Federated

Learning enables collaborative optimisation without transferring raw data.

2. Sensor Modalities

• Electrocardiogram (ECG)

• Electromyogram (EMG)

• Galvanic Skin Response (EDA)

• Airflow (respiration)

• Skin/body temperature

• Pulse and oxygen saturation (SpO )

• Body position detection

3. Revised Session Protocol (WESAD-Inspired)

The session protocol adopts a structured baseline–task–recovery design inspired by WESAD, while

remaining lightweight and repeatable. The emphasis is on controlled physiological perturbation rather than

inducing extreme psychological stress.

3.1 Phase definitions and timing

• Baseline (3 minutes): seated rest, normal breathing, minimal movement.

• Task (3 minutes): controlled perturbation using one of the defined tasks below.

• Recovery (3 minutes): seated rest to observe physiological recovery dynamics.

3.2 Task specification

• Mental arithmetic task: serial subtraction (e.g., 1000 − 7 repeatedly) performed silently.

• Respiratory task: paced breathing at a predefined rate (e.g., 6 breaths/min or 20 breaths/min).

Only one task type is used per session to ensure consistency across recordings. Task type and timing are

logged explicitly.

3.3 Ground-truth annotation

In addition to phase labels, a simple subjective rating (0–10) may be recorded at the end of each phase to

provide coarse ground-truth annotation without introducing participant burden.

4. Data Logging and Dataset Structure

Signals are logged as raw, time-stamped streams using a long-format schema to preserve fidelity and

accommodate heterogeneous sampling rates.

Long-format schema:

timestamp_ms, phase, sensor_type, value

5. Communication Overhead Definition and Measurement

Communication overhead is defined as the total number of bytes transmitted to support Federated

Learning model exchange and optional Digital Twin telemetry. Both uplink and downlink payloads are

considered.

5.1 Centralised and federated baselines

Centralised learning assumes transmission of raw data, while Federated Learning transmits only model

parameters or updates. Communication overhead is calculated using explicit byte counts under consistent

data representation assumptions.

5.2 Runtime measurement protocol

• Record payload size of each global model transmission.

• Record payload size of each local update.

• Optionally capture wire-level bytes using packet capture tools.

• Report per-client, per-round, and cumulative overhead.

6. Reporting and Reproducibility

All reported communication overhead values specify whether they represent payload-only or

payload-plus-header bytes. Session timing, task type, and sensor configuration are documented to ensure

reproducibility and comparability with simulation-based experiments.

Conclusion

The revised protocol strengthens behavioural control while preserving the original system-level focus. By

adopting a WESAD-inspired session structure, the experiment achieves improved comparability,

interpretability, and methodological clarity.