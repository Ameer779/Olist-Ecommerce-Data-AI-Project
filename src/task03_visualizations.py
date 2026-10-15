from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "cleaned_data"
OUTPUT_DIR = BASE_DIR / "reports" / "task03" / "visualizations"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_csv(filename):
    """Load a cleaned CSV dataset."""
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


def save_chart(filename):
    """Save the current chart as a PNG image."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"Saved: {filename}")


def main():
    print("Loading cleaned datasets...")

    orders = load_csv("olist_orders_cleaned.csv")
    items = load_csv("olist_order_items_cleaned.csv")
    payments = load_csv("olist_order_payments_cleaned.csv")
    reviews = load_csv("olist_order_reviews_cleaned.csv")
    products = load_csv("olist_products_cleaned.csv")
    translation = load_csv("product_category_translation_cleaned.csv")

    # 1. Bar chart: Top product categories by sales
    if {"product_id", "price"}.issubset(items.columns) and {
        "product_id", "product_category_name"
    }.issubset(products.columns):

        category_data = items.merge(
            products[["product_id", "product_category_name"]],
            on="product_id",
            how="left"
        )

        if {"product_category_name", "product_category_name_english"}.issubset(
            translation.columns
        ):
            category_data = category_data.merge(
                translation,
                on="product_category_name",
                how="left"
            )
            category_col = "product_category_name_english"
        else:
            category_col = "product_category_name"

        category_data[category_col] = (
            category_data[category_col].fillna("Unknown")
        )

        top_categories = (
            category_data.groupby(category_col)["price"]
            .sum()
            .nlargest(10)
            .sort_values()
        )

        plt.figure(figsize=(10, 6))
        plt.barh(top_categories.index, top_categories.values)
        plt.xlabel("Total Sales Value (R$)")
        plt.ylabel("Product Category")
        plt.title("Top 10 Product Categories by Sales")
        save_chart("01_top_categories_bar.png")

    # 2. Line chart: Monthly order trend
    if {"order_id", "order_purchase_timestamp"}.issubset(orders.columns):
        dates = pd.to_datetime(
            orders["order_purchase_timestamp"], errors="coerce"
        )
        monthly_orders = (
            orders.assign(month=dates.dt.to_period("M"))
            .dropna(subset=["month"])
            .groupby("month")["order_id"]
            .nunique()
        )

        if not monthly_orders.empty:
            plt.figure(figsize=(12, 5))
            plt.plot(
                monthly_orders.index.astype(str),
                monthly_orders.values,
                marker="o"
            )
            plt.xlabel("Month")
            plt.ylabel("Number of Orders")
            plt.title("Monthly Order Trend")
            plt.xticks(rotation=60)
            save_chart("02_monthly_orders_line.png")

    # 3. Pie chart: Payment method share by transaction count
    if {"payment_type", "payment_value"}.issubset(payments.columns):
        payment_counts = (
            payments["payment_type"]
            .fillna("Unknown")
            .value_counts()
        )

        if not payment_counts.empty:
            plt.figure(figsize=(8, 8))
            plt.pie(
                payment_counts.values,
                labels=payment_counts.index,
                autopct="%1.1f%%",
                startangle=90
            )
            plt.title("Share of Transactions by Payment Method")
            save_chart("03_payment_methods_pie.png")

    # 4. Histogram: Delivery time
    required_dates = {
        "order_purchase_timestamp",
        "order_delivered_customer_date"
    }

    if required_dates.issubset(orders.columns):
        purchased = pd.to_datetime(
            orders["order_purchase_timestamp"], errors="coerce"
        )
        delivered = pd.to_datetime(
            orders["order_delivered_customer_date"], errors="coerce"
        )

        delivery_days = (delivered - purchased).dt.total_seconds() / 86400
        delivery_days = delivery_days.dropna()
        delivery_days = delivery_days[delivery_days >= 0]

        if not delivery_days.empty:
            plt.figure(figsize=(9, 5))
            plt.hist(delivery_days, bins=30, edgecolor="black")
            plt.xlabel("Delivery Time (Days)")
            plt.ylabel("Number of Orders")
            plt.title("Distribution of Delivery Time")
            save_chart("04_delivery_time_histogram.png")

    # 5. Scatter plot: Product price vs freight
    if {"price", "freight_value"}.issubset(items.columns):
        scatter_data = items[["price", "freight_value"]].dropna()

        if not scatter_data.empty:
            # Limit plotted points for readability on large datasets.
            scatter_data = scatter_data.sample(
                n=min(5000, len(scatter_data)), random_state=42
            )

            plt.figure(figsize=(9, 6))
            plt.scatter(
                scatter_data["price"],
                scatter_data["freight_value"],
                alpha=0.45
            )
            plt.xlabel("Product Price (R$)")
            plt.ylabel("Freight Value (R$)")
            plt.title("Product Price vs Freight Value")
            save_chart("05_price_vs_freight_scatter.png")

    # 6. Bar chart: Customer review score distribution
    if "review_score" in reviews.columns:
        scores = pd.to_numeric(reviews["review_score"], errors="coerce")
        score_counts = scores.dropna().value_counts().sort_index()

        if not score_counts.empty:
            plt.figure(figsize=(8, 5))
            plt.bar(score_counts.index.astype(str), score_counts.values)
            plt.xlabel("Review Score")
            plt.ylabel("Number of Reviews")
            plt.title("Customer Review Score Distribution")
            save_chart("06_review_scores_bar.png")

    # 7. Bar chart: Total payment value by payment method
    if {"payment_type", "payment_value"}.issubset(payments.columns):
        payment_totals = (
            payments.assign(
                payment_value=pd.to_numeric(
                    payments["payment_value"], errors="coerce"
                )
            )
            .groupby("payment_type")["payment_value"]
            .sum()
            .dropna()
            .sort_values()
        )

        if not payment_totals.empty:
            plt.figure(figsize=(9, 5))
            plt.bar(payment_totals.index.astype(str), payment_totals.values)
            plt.xlabel("Payment Method")
            plt.ylabel("Total Payment Value (R$)")
            plt.title("Total Payment Value by Payment Method")
            plt.xticks(rotation=30, ha="right")
            save_chart("07_payment_value_bar.png")

    print("\nTask 03 visualization generation finished.")
    print(f"Charts folder: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()