import pandas as pd
from pathlib import Path

DATA_DIR = Path("Olist Brazilian E-Commerce Public")

csv_files = list(DATA_DIR.glob("*.csv"))

print("=" * 70)
print("OLIST DATASET - INITIAL QUALITY CHECK")
print("=" * 70)

print(f"\nTotal CSV files found: {len(csv_files)}")

for file in csv_files:
    print(f"\n{'-' * 70}")
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print(f"Missing values: {missing:,}")
    print(f"Duplicate rows: {duplicates:,}")

print("\n" + "=" * 70)
print("QUALITY CHECK COMPLETED")
print("=" * 70)
print("\n" + "=" * 70)
print("DETAILED MISSING VALUES BY COLUMN")
print("=" * 70)

for file in csv_files:
    df = pd.read_csv(file)

    missing_by_column = df.isnull().sum()
    missing_by_column = missing_by_column[missing_by_column > 0]

    if len(missing_by_column) > 0:
        print(f"\nFILE: {file.name}")
        print(missing_by_column)