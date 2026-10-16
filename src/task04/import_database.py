
import sqlite3
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_DIR / "cleaned_data"
DB_DIR = PROJECT_DIR / "database"
DB_PATH = DB_DIR / "olist_analysis.db"

DB_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "olist_customers_cleaned.csv": "customers",
    "olist_orders_cleaned.csv": "orders",
    "olist_order_items_cleaned.csv": "order_items",
    "olist_order_payments_cleaned.csv": "order_payments",
    "olist_order_reviews_cleaned.csv": "order_reviews",
    "olist_products_cleaned.csv": "products",
    "olist_sellers_cleaned.csv": "sellers",
    "olist_geolocation_cleaned.csv": "geolocation",
    "product_category_translation_cleaned.csv": "category_translation",
}

def main():
    print("Creating SQLite database...")
    print(f"Database location: {DB_PATH}")

    with sqlite3.connect(DB_PATH) as connection:
        for csv_file, table_name in FILES.items():
            csv_path = DATA_DIR / csv_file

            if not csv_path.exists():
                raise FileNotFoundError(
                    f"CSV file not found: {csv_path}"
                )

            print(f"Importing {csv_file}...")
            df = pd.read_csv(csv_path)

            df.to_sql(
                table_name,
                connection,
                if_exists="replace",
                index=False,
                chunksize=5000,
            )

            count = pd.read_sql_query(
                f'SELECT COUNT(*) AS total FROM "{table_name}"',
                connection,
            ).iloc[0]["total"]

            print(
                f"Table: {table_name} | Rows imported: {count:,}"
            )

    print("\nDatabase created successfully!")
    print(f"Saved at: {DB_PATH}")

if __name__ == "__main__":
    main()
