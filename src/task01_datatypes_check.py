import pandas as pd
from pathlib import Path

DATA_DIR = Path("cleaned_data")

print("=" * 80)
print("TASK 01 - DATA TYPES CHECK")
print("=" * 80)

for file in DATA_DIR.glob("*.csv"):
    df = pd.read_csv(file)

    print(f"\n{'-' * 80}")
    print(f"FILE: {file.name}")
    print("-" * 80)

    print(df.dtypes.to_string())

print("\n" + "=" * 80)
print("DATA TYPES CHECK COMPLETED")
print("=" * 80)