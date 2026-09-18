import pandas as pd
from pathlib import Path

# Folders
DATA_DIR = Path("Olist Brazilian E-Commerce Public")
OUTPUT_DIR = Path("cleaned_data")

OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 70)
print("OLIST DATASET - CLEANING")
print("=" * 70)


# --------------------------------------------------
# 1. CUSTOMERS
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_customers_dataset.csv")
before = len(df)

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_customers_cleaned.csv", index=False)

print(f"\nCustomers: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 2. GEOLOCATION
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_geolocation_dataset.csv")
before = len(df)

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_geolocation_cleaned.csv", index=False)

print(f"Geolocation: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 3. ORDERS
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_orders_dataset.csv")
before = len(df)

# Convert date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

# Missing dates are kept because they can represent
# orders that were not completed/delivered yet.

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_orders_cleaned.csv", index=False)

print(f"Orders: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 4. ORDER ITEMS
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_order_items_dataset.csv")
before = len(df)

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_order_items_cleaned.csv", index=False)

print(f"Order Items: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 5. ORDER PAYMENTS
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_order_payments_dataset.csv")

before = len(df)

# Payment installments cannot be zero
df.loc[df["payment_installments"] <= 0, "payment_installments"] = 1

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_order_payments_cleaned.csv", index=False)

print(f"Payments: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 6. ORDER REVIEWS
# --------------------------------------------------

df = pd.read_csv(DATA_DIR / "olist_order_reviews_dataset.csv")
before = len(df)

# Replace missing review text with a clear label
df["review_comment_title"] = df["review_comment_title"].fillna("No title")
df["review_comment_message"] = df["review_comment_message"].fillna("No review message")

df = df.drop_duplicates()

df.to_csv(
    OUTPUT_DIR / "olist_order_reviews_cleaned.csv",
    index=False
)

print(f"Reviews: {before:,} -> {len(df):,}")

# --------------------------------------------------
# 7. PRODUCTS
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_products_dataset.csv")
before = len(df)

# Missing category is labelled as Unknown
df["product_category_name"] = (
    df["product_category_name"].fillna("Unknown")
)

# Numerical missing values use median
numeric_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_products_cleaned.csv", index=False)

print(f"Products: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 8. SELLERS
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "olist_sellers_dataset.csv")
before = len(df)

df = df.drop_duplicates()

df.to_csv(OUTPUT_DIR / "olist_sellers_cleaned.csv", index=False)

print(f"Sellers: {before:,} -> {len(df):,}")


# --------------------------------------------------
# 9. CATEGORY TRANSLATION
# --------------------------------------------------
df = pd.read_csv(DATA_DIR / "product_category_name_translation.csv")
before = len(df)

df = df.drop_duplicates()

df.to_csv(
    OUTPUT_DIR / "product_category_translation_cleaned.csv",
    index=False
)

print(f"Category Translation: {before:,} -> {len(df):,}")


print("\n" + "=" * 70)
print("CLEANING COMPLETED SUCCESSFULLY")
print("=" * 70)
print(f"Cleaned files saved in: {OUTPUT_DIR}")