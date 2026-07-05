import pandas as pd

INPUT_FILE = "rows.csv"
OUTPUT_FILE = "complaints_clean.csv"
BAD_LINES_LOG = "bad_lines.log"

bad_line_count = [0]

def log_bad_line(bad_line):
    bad_line_count[0] += 1
    if bad_line_count[0] <= 20:  # just show first 20 examples
        print("Skipped line:", bad_line)
    return None  # tells pandas to skip it

print("Loading CSV... this may take a minute or two for ~700MB")
df = pd.read_csv(
    INPUT_FILE,
    dtype=str,
    engine="python",
    on_bad_lines=log_bad_line
)

print(f"Total bad lines skipped: {bad_line_count[0]:,}")
print(f"Loaded {len(df):,} rows, {len(df.columns)} columns")

if "Consumer complaint narrative" in df.columns:
    df = df.drop(columns=["Consumer complaint narrative"])
    print("Dropped 'Consumer complaint narrative' column")

df["Date received"] = pd.to_datetime(df["Date received"], errors="coerce")
before = len(df)
df = df.dropna(subset=["Date received"])
after = len(df)
print(f"Removed {before - after:,} rows with invalid/missing dates")

df.to_csv(OUTPUT_FILE, index=False)
print(f"Saved cleaned file as {OUTPUT_FILE} with {len(df):,} rows")