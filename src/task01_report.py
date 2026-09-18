import pandas as pd
from pathlib import Path

RAW_DIR = Path("Olist Brazilian E-Commerce Public")
CLEAN_DIR = Path("cleaned_data")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)

file_mapping = {
    "olist_customers_dataset.csv": "olist_customers_cleaned.csv",
    "olist_geolocation_dataset.csv": "olist_geolocation_cleaned.csv",
    "olist_orders_dataset.csv": "olist_orders_cleaned.csv",
    "olist_order_items_dataset.csv": "olist_order_items_cleaned.csv",
    "olist_order_payments_dataset.csv": "olist_order_payments_cleaned.csv",
    "olist_order_reviews_dataset.csv": "olist_order_reviews_cleaned.csv",
    "olist_products_dataset.csv": "olist_products_cleaned.csv",
    "olist_sellers_dataset.csv": "olist_sellers_cleaned.csv",
    "product_category_name_translation.csv": "product_category_translation_cleaned.csv"
}

report = []

for raw_file, clean_file in file_mapping.items():

    raw = pd.read_csv(RAW_DIR / raw_file)
    clean = pd.read_csv(CLEAN_DIR / clean_file)

    report.append({
        "Dataset": raw_file,
        "Before Rows": len(raw),
        "After Rows": len(clean),
        "Rows Removed": len(raw) - len(clean),
        "Before Missing": raw.isnull().sum().sum(),
        "After Missing": clean.isnull().sum().sum(),
        "Before Duplicates": raw.duplicated().sum(),
        "After Duplicates": clean.duplicated().sum()
    })

report_df = pd.DataFrame(report)

print("=" * 120)
print("TASK 01 - BEFORE / AFTER DATA QUALITY REPORT")
print("=" * 120)

print(report_df.to_string(index=False))

output_file = REPORT_DIR / "task01_before_after_report.csv"
report_df.to_csv(output_file, index=False)

print("\n" + "=" * 120)
print("REPORT SAVED SUCCESSFULLY")
print("=" * 120)
print(f"File: {output_file}")