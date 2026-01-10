import pandas as pd

BASE = "data/ecg/session01/"
IN_FILE = BASE + "ecg_session01_labeled.csv"
OUT_FILE = BASE + "ecg_session01_clean.csv"
REPORT_FILE = BASE + "ecg_session01_clean_report.txt"

OFFSETS = {"relax": 0, "stairs": 180000, "recovery": 360000}

def main():
    df = pd.read_csv(IN_FILE)

    df["timestamp_ms"] = pd.to_numeric(df["timestamp_ms"], errors="coerce")
    df["ecg_voltage"] = pd.to_numeric(df["ecg_voltage"], errors="coerce")
    df["phase"] = df["phase"].astype(str).str.strip().str.lower()

    df = df.dropna(subset=["timestamp_ms", "ecg_voltage", "phase"])
    df = df[df["phase"].isin(OFFSETS.keys())].copy()

    df["session_timestamp_ms"] = df.apply(
        lambda r: int(r["timestamp_ms"] + OFFSETS[r["phase"]]), axis=1
    )

    df = df.sort_values("session_timestamp_ms")
    df = df.drop_duplicates(subset=["session_timestamp_ms", "phase"], keep="first")

    df = df[["session_timestamp_ms", "phase", "ecg_voltage", "timestamp_ms"]]
    df.to_csv(OUT_FILE, index=False)

    mins = int(df["session_timestamp_ms"].min())
    maxs = int(df["session_timestamp_ms"].max())
    counts = df["phase"].value_counts().to_dict()

    with open(REPORT_FILE, "w") as f:
        f.write("ECG Session01 Clean Report\n")
        f.write("==========================\n")
        f.write("Input:  " + IN_FILE + "\n")
        f.write("Output: " + OUT_FILE + "\n\n")
        f.write("Rows per phase:\n")
        for k, v in counts.items():
            f.write(k + ": " + str(v) + "\n")
        f.write("\nTime range (session_timestamp_ms):\n")
        f.write("min=" + str(mins) + "  max=" + str(maxs) + "\n")
        f.write("\nExpected approx end ~ 540000 ms (9 minutes).\n")

    print("DONE")
    print("Saved:", OUT_FILE)
    print("Report:", REPORT_FILE)

if __name__ == "__main__":
    main()
