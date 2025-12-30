import pandas as pd

INFILE  = "data/gsr/session01/gsr_session01_labeled.csv"
OUTFILE = "data/gsr/session01/gsr_session01_clean.csv"
REPORT  = "data/gsr/session01/gsr_session01_clean_report.txt"

# Phase start offsets based on your notes:
# Relax 00:00, Stairs 03:00, Recovery 06:00 (in ms)
PHASE_OFFSET_MS = {
    "relax": 0,
    "stairs": 3 * 60 * 1000,
    "recovery": 6 * 60 * 1000,
}

df = pd.read_csv(INFILE)

# Standardise column names
df.columns = [c.strip() for c in df.columns]
if "GSR" in df.columns and "gsr" not in df.columns:
    df = df.rename(columns={"GSR":"gsr"})

# Keep only needed columns
df = df[["timestamp_ms","phase","gsr"]].copy()

# Basic cleaning: types + drop bad rows
df["phase"] = df["phase"].astype(str).str.strip().str.lower()
df["timestamp_ms"] = pd.to_numeric(df["timestamp_ms"], errors="coerce")
df["gsr"] = pd.to_numeric(df["gsr"], errors="coerce")
df = df.dropna(subset=["timestamp_ms","gsr","phase"])

# Add continuous session timestamp
df["phase_offset_ms"] = df["phase"].map(PHASE_OFFSET_MS)
missing = df["phase_offset_ms"].isna().sum()
if missing:
    unknown = sorted(df.loc[df["phase_offset_ms"].isna(), "phase"].unique().tolist())
    raise SystemExit(f"Unknown phase labels found: {unknown}. Expected: {list(PHASE_OFFSET_MS.keys())}")

df["session_timestamp_ms"] = (df["timestamp_ms"] + df["phase_offset_ms"]).astype(int)

# Sort + remove duplicates on the final timestamp (keep first)
df = df.sort_values(["session_timestamp_ms","phase"]).drop_duplicates(subset=["session_timestamp_ms"], keep="first")

# Reorder columns for downstream pipeline
df = df[["session_timestamp_ms","phase","gsr","timestamp_ms"]]

# Save
df.to_csv(OUTFILE, index=False)

# Simple report
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("GSR Session01 Clean Report\n")
    f.write("==========================\n")
    f.write(f"Input:  {INFILE}\n")
    f.write(f"Output: {OUTFILE}\n\n")
    f.write("Rows per phase:\n")
    f.write(df["phase"].value_counts().to_string())
    f.write("\n\nTime range (session_timestamp_ms):\n")
    f.write(f"min={df['session_timestamp_ms'].min()}  max={df['session_timestamp_ms'].max()}\n")
    f.write("\nExpected approx end ~ 540000 ms (9 minutes).\n")

print("DONE ✅")
print(f"Saved: {OUTFILE}")
print(f"Report: {REPORT}")
