# Step 6 — GSR Cleaning and Session Alignment (Session 01)

## Goal
Convert raw GSR streams into a single, continuous, **WESAD-inspired** session file with explicit phase labels, ready for downstream Digital Twin updates and Federated Learning experiments.

This session uses a controlled, repeatable protocol:
**3 min relax → 3 min stairs → 3 min recovery**.  
Phase timing is recorded in a session notes file. (See: `data/gsr/session01/gsr_session01_notes.txt`)

---

## Inputs (Session 01)
Raw phase files:
- `data/gsr/session01/gsr_raw_20251230_session01_relax.csv`
- `data/gsr/session01/gsr_raw_20251230_session01_stairs.csv`
- `data/gsr/session01/gsr_raw_20251230_session01_recovery.csv`

Session notes:
- `data/gsr/session01/gsr_session01_notes.txt`

Pre-labeled merge (if used):
- `data/gsr/session01/gsr_session01_labeled.csv`

---

## Cleaning + Alignment Output
Cleaned continuous session file:
- `data/gsr/session01/gsr_session01_clean.csv`

Clean report:
- `data/gsr/session01/gsr_session01_clean_report.txt`

---

## Output Columns (IMPORTANT)
The clean CSV contains **two timestamps by design**:

- `timestamp_ms`
  - Original device timestamp from the raw stream inside each phase file.
  - Useful for debugging and traceability back to the acquisition logs.

- `session_timestamp_ms`
  - A continuous session-level timestamp reconstructed using phase offsets
    (relax: 0 ms, stairs: 180,000 ms, recovery: 360,000 ms).


Other columns:
- `phase` = `relax` | `stairs` | `recovery`
- `gsr` = raw GSR value (as streamed)

---

## Validation Summary (Session 01)
Expected duration:
- ~540,000 ms (9 minutes total)

Observed (from clean report):
- Balanced samples per phase (≈ 900 each, at ~5 Hz)
- Continuous session_timestamp_ms coverage from ~0 to ~539,xxx ms

---

## Rationale
Separating:
1) raw acquisition  
2) protocol annotation (phase notes)  
3) cleaning + alignment  

ensures:
- reproducibility
- transparency
- auditability (raw ↔ clean trace)

This supports downstream **Digital Twin state updates** and **Federated Learning** experiments without making clinical diagnostic claims.

---

## Next Steps (not executed here)
- Optional light smoothing (for modelling only)
- Feature extraction / windowing (e.g., 5–15 second windows)
- Stream cleaned or windowed features into Ditto DT attributes
- Add the next sensor (one-by-one integration)
