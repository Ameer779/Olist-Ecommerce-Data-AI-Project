import pandas as pd
from pathlib import Path

RAW_DIR = Path("Olist Brazilian E-Commerce Public")
CLEAN_DIR = Path("cleaned_data")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)

results = []

for raw_file in RAW_DIR.glob("*.csv"):

    clean_name = raw_file.stem + "_cleaned.csv"

    if raw_file.name == "product_category_name_translation.csv":
        clean_name = "product_category_translation_cleaned.csv"

    clean_file = CLEAN_DIR / clean_name

    raw_df = pd.read_csv(raw_file)
    clean_df = pd.read_csv(clean_file)

    results.append({
        "Dataset": raw_file.name,
        "Before Rows": len(raw_df),
        "After Rows": len(clean_df),
        "Rows Removed": len(raw_df) - len(clean_df),
        "Before Missing": raw_df.isnull().sum().sum(),
        "After Missing": clean_df.isnull().sum().sum(),
        "Before Duplicates": raw_df.duplicated().sum(),
        "After Duplicates": clean_df.duplicated().sum()
    })

report = pd.DataFrame(results)

report.to_csv(
    REPORT_DIR / "task01_before_after_report.csv",
    index=False
)

print("=" * 80)
print("TASK 01 - BEFORE VS AFTER QUALITY REPORT")
print("=" * 80)

print(report.to_string(index=False))

print("\n" + "=" * 80)
print("REPORT SAVED:")
print("reports/task01_before_after_report.csv")
print("=" * 80)