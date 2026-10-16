import pandas as pd
from pathlib import Path

DATA_DIR = Path("cleaned_data")

# ---------------------------------------------------------
# 1. Inspect inconsistent order dates
# ---------------------------------------------------------
orders = pd.read_csv(DATA_DIR / "olist_orders_cleaned.csv")

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

problem_orders = orders[
    (orders["order_approved_at"] < orders["order_purchase_timestamp"]) |
    (orders["order_delivered_carrier_date"] < orders["order_approved_at"]) |
    (orders["order_delivered_customer_date"] < orders["order_delivered_carrier_date"])
]

print("=" * 80)
print("INCONSISTENT ORDER DATE RECORDS")
print("=" * 80)

print(f"Total problematic orders: {len(problem_orders)}")

print("\nFirst 10 records:")
print(
    problem_orders[
        [
            "order_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ].head(10).to_string(index=False)
)

# ---------------------------------------------------------
# 2. Inspect invalid payment installments
# ---------------------------------------------------------
payments = pd.read_csv(DATA_DIR / "olist_order_payments_cleaned.csv")

problem_payments = payments[
    payments["payment_installments"] <= 0
]

print("\n" + "=" * 80)
print("INVALID PAYMENT INSTALLMENTS")
print("=" * 80)

print(f"Total problematic payments: {len(problem_payments)}")

print("\nRecords:")
print(problem_payments.to_string(index=False))