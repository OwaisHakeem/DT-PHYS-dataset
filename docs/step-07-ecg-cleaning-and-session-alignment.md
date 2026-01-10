# Step 7 — ECG Cleaning and Session Alignment (Session 01)

## Goal
Convert raw ECG phase recordings into a single, continuous, **WESAD-inspired** session file with explicit phase labels and dual timestamps, suitable for Digital Twin state updates and Federated Learning pipelines.

This session follows a controlled protocol:
**3 min relax → 3 min stairs → 3 min recovery**

Phase timing is recorded in:
data/ecg/session01/ecg_session01_notes.txt

---

## Inputs (Session 01)

Raw phase files:
- data/ecg/session01/ECG_raw_20251230_session01_relax.csv
- data/ecg/session01/ECG_raw_20251230_session01_stairs.csv
- data/ecg/session01/ECG_raw_20251230_session01_recovery.csv

Merged labeled file:
- data/ecg/session01/ecg_session01_labeled.csv

Session notes:
- data/ecg/session01/ecg_session01_notes.txt

---

## Cleaning + Alignment Output

Cleaned continuous session:
- data/ecg/session01/ecg_session01_clean.csv

Cleaning report:
- data/ecg/session01/ecg_session01_clean_report.txt

Script used:
- scripts/clean_ecg_session01.py

---

## Output Columns (IMPORTANT)

The cleaned ECG CSV contains **two timestamps by design**:

- 	imestamp_ms
  - Original device timestamp from the ECG sensor within each phase file.
  - Used for traceability and debugging of raw acquisition.

- session_timestamp_ms
  - A reconstructed continuous session timeline across all phases.
  - Computed using fixed offsets:
    - relax = 0 ms
    - stairs = 180,000 ms
    - recovery = 360,000 ms

Other columns:
- phase = relax | stairs | recovery
- ecg_voltage = raw ECG voltage (V) as streamed from the e-Health board

This dual-timestamp approach allows:
- Accurate multi-sensor alignment
- Continuous Digital Twin state tracking
- Reproducible windowing for Federated Learning

---

## Validation Summary (Session 01)

From ecg_session01_clean_report.txt:

- Total session duration: ~539,000 ms (≈ 9 minutes)
- Rows per phase:
  - relax ≈ 64k
  - stairs ≈ 63k
  - recovery ≈ 63k
- Sampling rate: ~300–500 Hz (physiologically appropriate for ECG)
- Continuous session timeline from 0 → ~539,000 ms

The ECG signal exhibits:
- Stable baseline during relax
- Increased heart activity and motion artefacts during stairs
- Gradual recovery trend post-exertion

These are expected physiological patterns.

---

## Rationale

Separating:
- raw acquisition
- protocol annotation
- phase labeling
- continuous timeline reconstruction

ensures:
- full reproducibility
- transparent methodological justification
- compatibility with Digital Twin and Federated Learning pipelines

This dataset is **WESAD-inspired** but adapted to a physical-exertion protocol and is not intended for clinical diagnosis.

---

## Next Steps

- Feature extraction (R-peaks, HR, HRV, spectral features)
- Windowing for Federated Learning
- Live ECG stream integration into Ditto Digital Twin
- Addition of further sensors (SpO2, airflow, EMG, temperature)
