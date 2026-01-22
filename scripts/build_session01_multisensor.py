import pandas as pd

GSR_FILE = "data/gsr/session01-GSR/gsr_session01_clean.csv"
ECG_FILE = "data/ecg/session01/ecg_session01_clean.csv"
OUT_FILE = "data/session01/session01_multisensor_clean.csv"

def main():
    gsr = pd.read_csv(GSR_FILE)
    ecg = pd.read_csv(ECG_FILE)

    # Standardise column names for merging
    gsr = gsr.rename(columns={"gsr": "gsr"})
    ecg = ecg.rename(columns={"ecg_voltage": "ecg_raw"})

    # Keep only what we need
    gsr = gsr[["session_timestamp_ms", "phase", "gsr"]]
    ecg = ecg[["session_timestamp_ms", "phase", "ecg_raw"]]

    # Outer merge on session timestamp + phase
    merged = pd.merge(gsr, ecg, on=["session_timestamp_ms", "phase"], how="outer")

    # Sort and write
    merged = merged.sort_values(["session_timestamp_ms", "phase"])
    merged.to_csv(OUT_FILE, index=False)

    print("DONE ✅")
    print("GSR:", GSR_FILE)
    print("ECG:", ECG_FILE)
    print("Saved:", OUT_FILE)
    print("Columns:", merged.columns.tolist())
    print("Rows:", len(merged))

if __name__ == "__main__":
    main()
