import pandas as pd
from pathlib import Path

DATA_DIR = Path("cleaned_data")

print("=" * 80)
print("TASK 01 - INCORRECT / INCONSISTENT VALUES CHECK")
print("=" * 80)

# ---------------------------------------------------------
# 1. ORDERS CHECK
# ---------------------------------------------------------
orders = pd.read_csv(DATA_DIR / "olist_orders_cleaned.csv")

print("\n" + "-" * 80)
print("ORDERS CHECK")
print("-" * 80)

print("\nOrder Status Values:")
print(orders["order_status"].value_counts())

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

invalid_order_dates = (
    (orders["order_approved_at"] < orders["order_purchase_timestamp"]) |
    (orders["order_delivered_carrier_date"] < orders["order_approved_at"]) |
    (orders["order_delivered_customer_date"] < orders["order_delivered_carrier_date"])
).sum()

print(f"\nChronologically inconsistent order dates: {invalid_order_dates}")

# ---------------------------------------------------------
# 2. ORDER ITEMS CHECK
# ---------------------------------------------------------
items = pd.read_csv(DATA_DIR / "olist_order_items_cleaned.csv")

print("\n" + "-" * 80)
print("ORDER ITEMS CHECK")
print("-" * 80)

print(f"Negative price values: {(items['price'] < 0).sum()}")
print(f"Negative freight values: {(items['freight_value'] < 0).sum()}")
print(f"Invalid order item IDs: {(items['order_item_id'] <= 0).sum()}")

# ---------------------------------------------------------
# 3. PAYMENTS CHECK
# ---------------------------------------------------------
payments = pd.read_csv(DATA_DIR / "olist_order_payments_cleaned.csv")

print("\n" + "-" * 80)
print("PAYMENTS CHECK")
print("-" * 80)

print("\nPayment Types:")
print(payments["payment_type"].value_counts())

print(f"\nNegative payment values: {(payments['payment_value'] < 0).sum()}")
print(f"Invalid installments: {(payments['payment_installments'] <= 0).sum()}")

# ---------------------------------------------------------
# 4. REVIEWS CHECK
# ---------------------------------------------------------
reviews = pd.read_csv(DATA_DIR / "olist_order_reviews_cleaned.csv")

print("\n" + "-" * 80)
print("REVIEWS CHECK")
print("-" * 80)

print("\nReview Scores:")
print(reviews["review_score"].value_counts().sort_index())

invalid_scores = (
    (reviews["review_score"] < 1) |
    (reviews["review_score"] > 5)
).sum()

print(f"\nInvalid review scores: {invalid_scores}")

# ---------------------------------------------------------
# 5. PRODUCTS CHECK
# ---------------------------------------------------------
products = pd.read_csv(DATA_DIR / "olist_products_cleaned.csv")

print("\n" + "-" * 80)
print("PRODUCTS CHECK")
print("-" * 80)

numeric_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for col in numeric_columns:
    invalid = (products[col] < 0).sum()
    print(f"{col} - Negative values: {invalid}")

# ---------------------------------------------------------
# 6. GEOLOCATION CHECK
# ---------------------------------------------------------
geo = pd.read_csv(DATA_DIR / "olist_geolocation_cleaned.csv")

print("\n" + "-" * 80)
print("GEOLOCATION CHECK")
print("-" * 80)

invalid_lat = ((geo["geolocation_lat"] < -90) | (geo["geolocation_lat"] > 90)).sum()
invalid_lng = ((geo["geolocation_lng"] < -180) | (geo["geolocation_lng"] > 180)).sum()

print(f"Invalid latitude values: {invalid_lat}")
print(f"Invalid longitude values: {invalid_lng}")

print("\n" + "=" * 80)
print("INCONSISTENT VALUES CHECK COMPLETED")
print("=" * 80)