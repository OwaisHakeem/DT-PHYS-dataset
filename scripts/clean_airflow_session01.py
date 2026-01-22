import pandas as pd

BASE = "data/airflow/session01/"
IN_FILE = BASE + "airflow_session01_labeled.csv"
OUT_FILE = BASE + "airflow_session01_clean.csv"
REPORT_FILE = BASE + "airflow_session01_clean_report.txt"

OFFSETS = {"relax": 0, "stairs": 180000, "recovery": 360000}

def main():
    df = pd.read_csv(IN_FILE)
    df.columns = [c.strip().lower() for c in df.columns]

    ts_col = [c for c in df.columns if "timestamp" in c][0]
    val_col = [c for c in df.columns if c not in [ts_col, "phase"]][0]

    df = df.rename(columns={
        ts_col: "timestamp_ms",
        val_col: "airflow_raw"
    })

    df["timestamp_ms"] = pd.to_numeric(df["timestamp_ms"], errors="coerce")
    df["airflow_raw"] = pd.to_numeric(df["airflow_raw"], errors="coerce")
    df["phase"] = df["phase"].astype(str).str.strip().str.lower()

    df = df.dropna(subset=["timestamp_ms", "airflow_raw", "phase"])
    df = df[df["phase"].isin(OFFSETS.keys())].copy()

    df["session_timestamp_ms"] = df.apply(
        lambda r: int(r["timestamp_ms"] + OFFSETS[r["phase"]]),
        axis=1
    )

    df = df.sort_values("session_timestamp_ms")
    df = df.drop_duplicates(
        subset=["session_timestamp_ms", "phase"],
        keep="first"
    )

    out = df[
        ["session_timestamp_ms", "phase", "airflow_raw", "timestamp_ms"]
    ]

    out.to_csv(OUT_FILE, index=False)

    mins = int(out["session_timestamp_ms"].min())
    maxs = int(out["session_timestamp_ms"].max())
    counts = out["phase"].value_counts().to_dict()

    with open(REPORT_FILE, "w") as f:
        f.write("Airflow Session01 Clean Report\n")
        f.write("==============================\n")
        f.write("Input:  " + IN_FILE + "\n")
        f.write("Output: " + OUT_FILE + "\n\n")
        f.write("Rows per phase:\n")
        for k, v in counts.items():
            f.write(f"{k}: {v}\n")
        f.write("\nTime range (session_timestamp_ms):\n")
        f.write(f"min={mins}  max={maxs}\n")
        f.write("\nExpected approx end ~ 540000 ms (9 minutes).\n")

    print("DONE ✅")
    print("Saved:", OUT_FILE)
    print("Report:", REPORT_FILE)


if __name__ == "__main__":
    main()
