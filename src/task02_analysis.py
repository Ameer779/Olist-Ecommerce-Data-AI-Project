"""
Task 02 — Analyze Data Using Python
Olist E-Commerce Data & AI Internship Project

Tools:
- Python
- Pandas
- NumPy
- Matplotlib

This script uses the cleaned datasets created in Task 01.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# Project root = Olist-Ecommerce-Data-AI-Project
BASE_DIR = Path(__file__).resolve().parent.parent

CLEANED_DIR = BASE_DIR / "cleaned_data"

TASK02_DIR = BASE_DIR / "reports" / "task02"
STATISTICS_DIR = TASK02_DIR / "statistics"
VISUALIZATIONS_DIR = TASK02_DIR / "visualizations"
FINDINGS_DIR = TASK02_DIR / "findings"

STATISTICS_DIR.mkdir(parents=True, exist_ok=True)
VISUALIZATIONS_DIR.mkdir(parents=True, exist_ok=True)
FINDINGS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. HELPER FUNCTIONS
# ============================================================

def load_csv(filename):
    """Load a cleaned CSV file from cleaned_data."""
    path = CLEANED_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"\nFile not found:\n{path}\n"
            f"Please check the cleaned_data folder."
        )

    return pd.read_csv(path)


def save_plot(filename):
    """Save and close the current matplotlib figure."""
    path = VISUALIZATIONS_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved visualization: {path.name}")


# ============================================================
# 3. START
# ============================================================

print("=" * 70)
print("TASK 02 — ANALYZE DATA USING PYTHON")
print("Olist E-Commerce Data & AI Internship Project")
print("=" * 70)


# ============================================================
# 4. LOAD CLEANED DATASETS
# ============================================================

print("\n[1/10] Loading cleaned datasets...")

customers = load_csv("olist_customers_cleaned.csv")
geolocation = load_csv("olist_geolocation_cleaned.csv")
orders = load_csv("olist_orders_cleaned.csv")
order_items = load_csv("olist_order_items_cleaned.csv")
payments = load_csv("olist_order_payments_cleaned.csv")
reviews = load_csv("olist_order_reviews_cleaned.csv")
products = load_csv("olist_products_cleaned.csv")
sellers = load_csv("olist_sellers_cleaned.csv")
category_translation = load_csv(
    "product_category_translation_cleaned.csv"
)

datasets = {
    "customers": customers,
    "geolocation": geolocation,
    "orders": orders,
    "order_items": order_items,
    "payments": payments,
    "reviews": reviews,
    "products": products,
    "sellers": sellers,
    "category_translation": category_translation,
}

print("\nDatasets loaded successfully:")

for name, df in datasets.items():
    print(
        f"{name:25s} "
        f"{df.shape[0]:>8,} rows × {df.shape[1]:>3} columns"
    )


# ============================================================
# 5. CONVERT DATA TYPES
# ============================================================

print("\n[2/10] Preparing data types...")

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

for column in date_columns:
    if column in orders.columns:
        orders[column] = pd.to_datetime(
            orders[column],
            errors="coerce"
        )

numeric_columns = [
    "price",
    "freight_value",
]

for column in numeric_columns:
    if column in order_items.columns:
        order_items[column] = pd.to_numeric(
            order_items[column],
            errors="coerce"
        )

if "payment_value" in payments.columns:
    payments["payment_value"] = pd.to_numeric(
        payments["payment_value"],
        errors="coerce"
    )

if "review_score" in reviews.columns:
    reviews["review_score"] = pd.to_numeric(
        reviews["review_score"],
        errors="coerce"
    )


# ============================================================
# 6. BASIC STATISTICS
# ============================================================

print("\n[3/10] Calculating basic statistics...")

numeric_datasets = {
    "order_items": order_items,
    "payments": payments,
    "reviews": reviews,
    "products": products,
}

for name, df in numeric_datasets.items():

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.shape[1] > 0:

        statistics = numeric_df.describe().T

        output = STATISTICS_DIR / f"{name}_basic_statistics.csv"

        statistics.to_csv(output)

        print(f"Saved statistics: {output.name}")


# ============================================================
# 7. BUSINESS STATISTICS
# ============================================================

business_statistics = []

if "price" in order_items.columns:

    business_statistics.append(
        ["Total Product Sales",
         order_items["price"].sum()]
    )

    business_statistics.append(
        ["Average Product Price",
         order_items["price"].mean()]
    )

    business_statistics.append(
        ["Minimum Product Price",
         order_items["price"].min()]
    )

    business_statistics.append(
        ["Maximum Product Price",
         order_items["price"].max()]
    )


if "freight_value" in order_items.columns:

    business_statistics.append(
        ["Total Freight Value",
         order_items["freight_value"].sum()]
    )

    business_statistics.append(
        ["Average Freight Value",
         order_items["freight_value"].mean()]
    )


if "payment_value" in payments.columns:

    business_statistics.append(
        ["Total Payment Value",
         payments["payment_value"].sum()]
    )

    business_statistics.append(
        ["Average Payment Value",
         payments["payment_value"].mean()]
    )


if "review_score" in reviews.columns:

    business_statistics.append(
        ["Average Review Score",
         reviews["review_score"].mean()]
    )


business_statistics_df = pd.DataFrame(
    business_statistics,
    columns=["Metric", "Value"]
)

business_statistics_df.to_csv(
    STATISTICS_DIR / "business_statistics.csv",
    index=False
)

print("Saved: business_statistics.csv")


# ============================================================
# 8. HIGHEST / LOWEST VALUES
# ============================================================

print("\n[4/10] Finding highest and lowest values...")

if "price" in order_items.columns:

    highest_prices = order_items.nlargest(
        10,
        "price"
    )

    lowest_prices = order_items.nsmallest(
        10,
        "price"
    )

    highest_prices.to_csv(
        STATISTICS_DIR / "top_10_highest_price_items.csv",
        index=False
    )

    lowest_prices.to_csv(
        STATISTICS_DIR / "top_10_lowest_price_items.csv",
        index=False
    )

    print("Saved highest/lowest product price analysis.")


if "payment_value" in payments.columns:

    highest_payments = payments.nlargest(
        10,
        "payment_value"
    )

    highest_payments.to_csv(
        STATISTICS_DIR / "top_10_highest_payment_values.csv",
        index=False
    )

    print("Saved highest payment values.")


# ============================================================
# 9. PRODUCT CATEGORY ANALYSIS
# ============================================================

print("\n[5/10] Analyzing product categories...")

category_data = order_items.merge(
    products,
    on="product_id",
    how="left"
)

if "product_category_name" in category_data.columns:

    if "product_category_name" in category_translation.columns:

        category_data = category_data.merge(
            category_translation,
            on="product_category_name",
            how="left",
            suffixes=("", "_translation")
        )

    if "product_category_name_english" in category_data.columns:

        category_column = "product_category_name_english"

    else:

        category_column = "product_category_name"

    category_analysis = (
        category_data
        .groupby(category_column)
        .agg(
            number_of_items=("order_id", "count"),
            total_sales=("price", "sum"),
            average_price=("price", "mean"),
            total_freight=("freight_value", "sum")
        )
        .sort_values(
            "total_sales",
            ascending=False
        )
    )

    category_analysis.to_csv(
        STATISTICS_DIR / "sales_by_product_category.csv"
    )

    print("\nTop 10 categories by sales:")

    print(
        category_analysis
        .head(10)
        .round(2)
        .to_string()
    )

    # Visualization

    top_categories = (
        category_analysis
        .head(10)
        .sort_values("total_sales")
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        top_categories.index.astype(str),
        top_categories["total_sales"]
    )

    plt.xlabel("Sales Value (R$)")
    plt.ylabel("Product Category")
    plt.title("Top 10 Product Categories by Sales")

    save_plot(
        "01_top_10_product_categories_by_sales.png"
    )


# ============================================================
# 10. PAYMENT METHOD ANALYSIS
# ============================================================

print("\n[6/10] Analyzing payment methods...")

if {
    "payment_type",
    "payment_value"
}.issubset(payments.columns):

    payment_analysis = (
        payments
        .groupby("payment_type")
        .agg(
            transactions=("order_id", "count"),
            unique_orders=("order_id", "nunique"),
            total_value=("payment_value", "sum"),
            average_value=("payment_value", "mean")
        )
        .sort_values(
            "total_value",
            ascending=False
        )
    )

    payment_analysis.to_csv(
        STATISTICS_DIR / "payment_method_analysis.csv"
    )

    print("\nPayment method analysis:")

    print(
        payment_analysis
        .round(2)
        .to_string()
    )

    plt.figure(figsize=(9, 5))

    plt.bar(
        payment_analysis.index.astype(str),
        payment_analysis["total_value"]
    )

    plt.xlabel("Payment Method")
    plt.ylabel("Total Payment Value (R$)")
    plt.title("Total Payment Value by Payment Method")

    plt.xticks(
        rotation=30,
        ha="right"
    )

    save_plot(
        "02_payment_method_analysis.png"
    )


# ============================================================
# 11. MONTHLY ORDER TREND
# ============================================================

print("\n[7/10] Analyzing monthly order trends...")

if {
    "order_id",
    "order_purchase_timestamp"
}.issubset(orders.columns):

    time_orders = orders.dropna(
        subset=["order_purchase_timestamp"]
    ).copy()

    time_orders["year_month"] = (
        time_orders[
            "order_purchase_timestamp"
        ]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_orders = (
        time_orders
        .groupby("year_month")
        .agg(
            orders=("order_id", "nunique"),
            customers=("customer_id", "nunique")
        )
        .reset_index()
    )

    monthly_orders.to_csv(
        STATISTICS_DIR / "monthly_order_trend.csv",
        index=False
    )

    print("\nMonthly order trend:")

    print(
        monthly_orders
        .to_string(index=False)
    )

    plt.figure(figsize=(12, 5))

    plt.plot(
        monthly_orders["year_month"],
        monthly_orders["orders"],
        marker="o"
    )

    plt.xlabel("Month")
    plt.ylabel("Number of Orders")
    plt.title("Monthly Order Trend")

    plt.xticks(rotation=60)

    save_plot(
        "03_monthly_order_trend.png"
    )


# ============================================================
# 12. MONTHLY SALES TREND
# ============================================================

print("\n[8/10] Analyzing monthly sales trends...")

if {
    "order_id",
    "price"
}.issubset(order_items.columns) and {
    "order_id",
    "order_purchase_timestamp"
}.issubset(orders.columns):

    sales_data = order_items.merge(
        orders[
            [
                "order_id",
                "order_purchase_timestamp"
            ]
        ],
        on="order_id",
        how="left"
    )

    sales_data = sales_data.dropna(
        subset=["order_purchase_timestamp"]
    )

    sales_data["year_month"] = (
        sales_data[
            "order_purchase_timestamp"
        ]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_sales = (
        sales_data
        .groupby("year_month")
        .agg(
            sales=("price", "sum"),
            items=("order_id", "count")
        )
        .reset_index()
    )

    monthly_sales.to_csv(
        STATISTICS_DIR / "monthly_sales_trend.csv",
        index=False
    )

    plt.figure(figsize=(12, 5))

    plt.plot(
        monthly_sales["year_month"],
        monthly_sales["sales"],
        marker="o"
    )

    plt.xlabel("Month")
    plt.ylabel("Sales Value (R$)")
    plt.title("Monthly Sales Trend")

    plt.xticks(rotation=60)

    save_plot(
        "04_monthly_sales_trend.png"
    )


# ============================================================
# 13. REVIEW SCORE ANALYSIS
# ============================================================

print("\n[9/10] Analyzing customer reviews...")

if "review_score" in reviews.columns:

    review_distribution = (
        reviews["review_score"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    review_distribution.columns = [
        "review_score",
        "number_of_reviews"
    ]

    review_distribution.to_csv(
        STATISTICS_DIR / "review_score_distribution.csv",
        index=False
    )

    print("\nReview score distribution:")

    print(
        review_distribution
        .to_string(index=False)
    )

    average_review = reviews[
        "review_score"
    ].mean()

    print(
        f"\nAverage review score: "
        f"{average_review:.2f} / 5"
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        review_distribution["review_score"].astype(str),
        review_distribution["number_of_reviews"]
    )

    plt.xlabel("Review Score")
    plt.ylabel("Number of Reviews")
    plt.title("Customer Review Score Distribution")

    save_plot(
        "05_review_score_distribution.png"
    )


# ============================================================
# 14. PRICE VS FREIGHT RELATIONSHIP
# ============================================================

print("\n[10/10] Analyzing relationships between variables...")

correlations = []

if {
    "price",
    "freight_value"
}.issubset(order_items.columns):

    relationship_data = order_items[
        [
            "price",
            "freight_value"
        ]
    ].dropna()

    price_freight_corr = (
        relationship_data["price"]
        .corr(
            relationship_data["freight_value"]
        )
    )

    correlations.append(
        [
            "Product Price vs Freight Value",
            price_freight_corr
        ]
    )

    print(
        f"Price vs freight correlation: "
        f"{price_freight_corr:.4f}"
    )

    # Use sample for visualization if dataset is large

    sample = relationship_data.sample(
        min(5000, len(relationship_data)),
        random_state=42
    )

    plt.figure(figsize=(9, 6))

    plt.scatter(
        sample["price"],
        sample["freight_value"],
        alpha=0.35
    )

    plt.xlabel("Product Price (R$)")
    plt.ylabel("Freight Value (R$)")
    plt.title(
        "Relationship Between Product Price and Freight Value"
    )

    save_plot(
        "06_price_vs_freight_relationship.png"
    )


# ============================================================
# 15. DELIVERY TIME ANALYSIS
# ============================================================

delivery_data = None

if {
    "order_purchase_timestamp",
    "order_delivered_customer_date"
}.issubset(orders.columns):

    delivery_data = orders.dropna(
        subset=[
            "order_purchase_timestamp",
            "order_delivered_customer_date"
        ]
    ).copy()

    delivery_data["delivery_days"] = (
        delivery_data[
            "order_delivered_customer_date"
        ]
        - delivery_data[
            "order_purchase_timestamp"
        ]
    ).dt.total_seconds() / 86400

    delivery_data = delivery_data[
        delivery_data["delivery_days"] >= 0
    ]

    delivery_statistics = (
        delivery_data["delivery_days"]
        .describe()
    )

    delivery_statistics.to_csv(
        STATISTICS_DIR / "delivery_time_statistics.csv"
    )

    print("\nDelivery time statistics:")

    print(
        delivery_statistics
        .round(2)
        .to_string()
    )

    plt.figure(figsize=(9, 5))

    plt.hist(
        delivery_data["delivery_days"],
        bins=30
    )

    plt.xlabel("Delivery Time (Days)")
    plt.ylabel("Number of Orders")
    plt.title("Distribution of Delivery Time")

    save_plot(
        "07_delivery_time_distribution.png"
    )


# ============================================================
# 16. IMPORTANT FINDINGS
# ============================================================

print("\n" + "=" * 70)
print("IMPORTANT FINDINGS")
print("=" * 70)

findings = []


# Finding 1 — Product category

if "category_analysis" in locals():

    top_category = category_analysis.iloc[0]

    findings.append(
        f"1. The highest-sales product category is "
        f"'{category_analysis.index[0]}', generating approximately "
        f"R$ {top_category['total_sales']:,.2f} in sales."
    )


# Finding 2 — Payment method

if "payment_analysis" in locals():

    top_payment = payment_analysis.iloc[0]

    findings.append(
        f"2. '{payment_analysis.index[0]}' is the payment method "
        f"with the highest total payment value, approximately "
        f"R$ {top_payment['total_value']:,.2f}."
    )


# Finding 3 — Review score

if "review_score" in reviews.columns:

    average_score = reviews[
        "review_score"
    ].mean()

    findings.append(
        f"3. The average customer review score is "
        f"{average_score:.2f} out of 5."
    )


# Finding 4 — Delivery time

if delivery_data is not None and len(delivery_data) > 0:

    average_delivery = (
        delivery_data["delivery_days"].mean()
    )

    median_delivery = (
        delivery_data["delivery_days"].median()
    )

    findings.append(
        f"4. The average delivery time is "
        f"{average_delivery:.1f} days, while the median "
        f"delivery time is {median_delivery:.1f} days."
    )


# Finding 5 — Price/freight

if "price_freight_corr" in locals():

    findings.append(
        f"5. Product price and freight value have a "
        f"correlation of {price_freight_corr:.3f}, indicating "
        f"the strength and direction of their relationship."
    )


# Finding 6 — Peak month

if "monthly_orders" in locals():

    peak_month = monthly_orders.loc[
        monthly_orders["orders"].idxmax()
    ]

    findings.append(
        f"6. The highest number of orders occurred in "
        f"{peak_month['year_month']}, with "
        f"{int(peak_month['orders']):,} orders."
    )


for finding in findings:
    print(f"\n{finding}")


# Save findings

with open(
    FINDINGS_DIR / "task02_important_findings.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "TASK 02 — IMPORTANT FINDINGS\n"
    )

    file.write("=" * 60 + "\n\n")

    for finding in findings:
        file.write(
            finding + "\n\n"
        )


# Save correlations

if correlations:

    correlation_df = pd.DataFrame(
        correlations,
        columns=[
            "Relationship",
            "Correlation"
        ]
    )

    correlation_df.to_csv(
        STATISTICS_DIR / "relationship_correlations.csv",
        index=False
    )


# ============================================================
# 17. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("TASK 02 COMPLETED SUCCESSFULLY")
print("=" * 70)

print(
    f"\nResults saved in:\n"
    f"{TASK02_DIR}"
)

print(
    "\nGenerated folders:"
)

print(
    f"  Statistics:      {STATISTICS_DIR}"
)

print(
    f"  Visualizations:  {VISUALIZATIONS_DIR}"
)

print(
    f"  Findings:        {FINDINGS_DIR}"
)

print("\nTask 02 requirements completed:")
print("  ✓ Basic statistics")
print("  ✓ Highest and lowest values")
print("  ✓ Grouping and comparisons")
print("  ✓ Trend analysis")
print("  ✓ Relationship analysis")
print("  ✓ Visualizations")
print("  ✓ 3+ important findings")

print("\n" + "=" * 70)