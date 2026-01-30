# eHealth Digital Twin + Federated Learning (DT–FL)

A research-grade multisensor physiological data pipeline designed for Digital Twin modelling and Federated Learning experiments.

---

## Project Overview

This repository presents a reproducible framework for collecting, cleaning, aligning, and fusing physiological sensor data. The project supports advanced experimentation in Digital Twin technologies and privacy-preserving machine learning.

The focus is on transparency, scientific reproducibility, and ethical non-diagnostic research use.

---

## Project Objectives

- Build a clean multisensor physiological dataset
- Align heterogeneous sensor streams using a unified session timeline
- Prepare structured data for Digital Twin modelling
- Simulate live sensor telemetry from offline datasets
- Enable Federated Learning without centralising raw data

---

## Experimental Protocol

Each session follows a structured 3–3–3 protocol:

Relax – 3 minutes  
Physical stress (stairs) – 3 minutes  
Recovery – 3 minutes  

Total duration: 9 minutes  
Aligned timeline: 0–540,000 ms

---

## Sensors Included

GSR (EDA) – Skin conductance and stress response  
ECG – Cardiac waveform signal  
Airflow – Respiratory amplitude variability  

Timestamps preserved:
- timestamp_ms (device-local)
- session_timestamp_ms (aligned timeline)

---

## Repository Structure

arduino/          Arduino sketches  
scripts/          Data cleaning and fusion scripts  
docs/             Step-by-step technical documentation  
public_data/      Published processed dataset  
environment/      Python dependencies  

---

## Dataset

Cleaned datasets are available in:

public_data/session01/

Files included:
- gsr_session01_clean.csv  
- ecg_session01_clean.csv  
- airflow_session01_clean.csv  
- session01_multisensor_clean.csv  

Raw data is intentionally excluded.

---

## Multisensor Fusion Strategy

- Different sampling rates per sensor
- Time-aligned using session timestamps
- Outer join strategy
- Missing values retained as NaN
- No interpolation applied

---

## Digital Twin (Next Phase)

Digital Twin modelling will be implemented using Eclipse Ditto.

Each session will be represented as a virtual physiological entity receiving time-indexed updates.

---

## Federated Learning (Next Phase)

Federated Learning will be implemented using live-style simulation:

- Each session acts as a client
- Local training on time windows
- Only model parameters shared
- Central aggregation (FedAvg)

---

## Reproducibility

Install dependencies:

pip install -r environment/requirements.txt

Run multisensor fusion:

python scripts/build_session01_multisensor.py

---

## Ethics

This project is for research and educational purposes only.  
Not intended for clinical diagnosis or medical decision-making.

---

## Citation

Please cite this work using the provided CITATION.cff.

---

## License

MIT License

---

## Maintainer

Owais Hakeem