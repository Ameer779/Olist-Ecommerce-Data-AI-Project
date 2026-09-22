# Olist E-Commerce Data & AI Project

A data analysis and AI-focused project based on the **Olist Brazilian E-Commerce Public Dataset**.

This project is being completed as part of a **Data & AI Internship** and currently includes data cleaning, quality checking, statistical analysis, business insights, and data visualization.

---

## Project Overview

The project analyzes the Olist Brazilian E-Commerce Public Dataset to understand data quality, business performance, sales trends, payment methods, customer reviews, product categories, pricing, freight, and delivery performance.

The project is divided into multiple tasks:

* **Task 01:** Data Cleaning & Quality Checking
* **Task 02:** Exploratory Data Analysis & Business Insights

---

# Task 01 — Data Cleaning & Quality Checking

## Task 01 Objectives

* Load the datasets using Python and Pandas
* Identify missing values
* Remove duplicate records
* Handle incorrect or inconsistent values
* Validate and correct data types
* Export cleaned datasets
* Generate a before/after data-quality report

## Dataset

The project uses the Olist Brazilian E-Commerce Public Dataset containing 9 CSV files:

* Customers
* Geolocation
* Orders
* Order Items
* Order Payments
* Order Reviews
* Products
* Sellers
* Product Category Translation

The original dataset files are not included in this public repository because of their large size. They were kept locally during the analysis process.

## Data Cleaning Performed

### Missing Values

Missing values were identified in the Orders, Reviews, and Products datasets.

* Missing review titles were replaced with `No title`.
* Missing review messages were replaced with `No review message`.
* Missing product categories were replaced with `Unknown`.
* Missing numerical product values were handled using median values.
* Missing order lifecycle timestamps were retained because they can represent incomplete stages of an order rather than invalid records.

### Duplicate Records

Duplicate records were checked across all datasets.

The main duplicate issue was found in the geolocation dataset:

* Before: 1,000,163 records
* Duplicates removed: 261,831
* After: 738,332 records

### Incorrect and Inconsistent Values

The following checks were performed:

* Negative order item prices
* Negative freight values
* Invalid order item IDs
* Negative payment values
* Invalid payment installments
* Invalid review scores
* Negative product measurements
* Invalid latitude and longitude values
* Order status values
* Order date inconsistencies

Two payment records had zero installments and were corrected to one installment.

Order date inconsistencies were reviewed and retained because they appeared to be timestamp lifecycle issues rather than clear evidence that the complete order records were invalid.

---

## Task 01 Before / After Summary

| Dataset              | Before Rows | After Rows | Rows Removed |
| -------------------- | ----------: | ---------: | -----------: |
| Customers            |      99,441 |     99,441 |            0 |
| Geolocation          |   1,000,163 |    738,332 |      261,831 |
| Orders               |      99,441 |     99,441 |            0 |
| Order Items          |     112,650 |    112,650 |            0 |
| Order Payments       |     103,886 |    103,886 |            0 |
| Order Reviews        |      99,224 |     99,224 |            0 |
| Products             |      32,951 |     32,951 |            0 |
| Sellers              |       3,095 |      3,095 |            0 |
| Category Translation |          71 |         71 |            0 |

---

# Task 02 — Exploratory Data Analysis & Business Insights

## Task 02 Objectives

Task 02 focuses on exploring the cleaned Olist data and generating meaningful statistical and business insights.

The analysis includes:

* Basic statistical analysis
* Sales analysis
* Product category analysis
* Payment method analysis
* Monthly order trends
* Monthly sales trends
* Review score distribution
* Delivery time analysis
* Product price analysis
* Freight analysis
* Correlation analysis
* Identification of important business findings
* Data visualization

## Task 02 Analysis Performed

### Business Statistics

General business statistics were calculated to understand the overall structure and performance of the e-commerce dataset.

### Sales by Product Category

Product categories were analyzed to identify categories with higher sales activity.

### Payment Method Analysis

Payment methods were analyzed to understand the distribution of customer payment preferences.

### Monthly Order Trend

Orders were analyzed over time to identify changes and patterns in monthly order volume.

### Monthly Sales Trend

Monthly sales were calculated and visualized to examine sales patterns over time.

### Review Score Distribution

Customer review scores were analyzed to understand customer satisfaction patterns.

### Delivery Time Analysis

Delivery time statistics were calculated to examine the distribution and performance of order deliveries.

### Product Price and Freight Analysis

Product prices and freight values were analyzed to understand their relationship and distribution.

### Correlation Analysis

Relationships between important numerical variables were examined using correlation analysis.

---

## Task 02 Visualizations

The project includes the following visualizations:

1. Top 10 Product Categories by Sales
2. Payment Method Analysis
3. Monthly Order Trend
4. Monthly Sales Trend
5. Review Score Distribution
6. Price vs Freight Relationship
7. Delivery Time Distribution

All Task 02 visualizations are available in:

```text
reports/task02/visualizations/
```

---

## Task 02 Statistical Reports

The statistical outputs are stored in:

```text
reports/task02/statistics/
```

The reports include:

* Business statistics
* Delivery time statistics
* Monthly order trend
* Monthly sales trend
* Order items basic statistics
* Payment method analysis
* Payment statistics
* Product statistics
* Relationship correlations
* Review score distribution
* Review statistics
* Sales by product category
* Top 10 highest payment values
* Top 10 highest price items
* Top 10 lowest price items

Important findings are also documented in:

```text
reports/task02/findings/task02_important_findings.txt
```

---

# Project Structure

```text
Olist-Ecommerce-Data-AI-Project/
│
├── reports/
│   │
│   ├── task01_before_after_report.csv
│   │
│   └── task02/
│       ├── findings/
│       │   └── task02_important_findings.txt
│       │
│       ├── statistics/
│       │   ├── business_statistics.csv
│       │   ├── delivery_time_statistics.csv
│       │   ├── monthly_order_trend.csv
│       │   ├── monthly_sales_trend.csv
│       │   ├── order_items_basic_statistics.csv
│       │   ├── payment_method_analysis.csv
│       │   ├── payments_basic_statistics.csv
│       │   ├── products_basic_statistics.csv
│       │   ├── relationship_correlations.csv
│       │   ├── review_score_distribution.csv
│       │   ├── reviews_basic_statistics.csv
│       │   ├── sales_by_product_category.csv
│       │   ├── top_10_highest_payment_values.csv
│       │   ├── top_10_highest_price_items.csv
│       │   └── top_10_lowest_price_items.csv
│       │
│       └── visualizations/
│           ├── 01_top_10_product_categories_by_sales.png
│           ├── 02_payment_method_analysis.png
│           ├── 03_monthly_order_trend.png
│           ├── 04_monthly_sales_trend.png
│           ├── 05_review_score_distribution.png
│           ├── 06_price_vs_freight_relationship.png
│           └── 07_delivery_time_distribution.png
│
├── src/
│   ├── clean_dataset.py
│   ├── task01_quality_check.py
│   ├── task01_datatypes_check.py
│   ├── task01_inconsistent_check.py
│   ├── task01_problem_records.py
│   ├── task01_report.py
│   └── task02_analysis.py
│
├── .gitignore
└── README.md
```

---

# Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* CSV
* Git
* GitHub
* Exploratory Data Analysis
* Statistical Analysis
* Data Visualization

---

# Project Deliverables

## Task 01

* Python data-cleaning scripts
* Data-quality checking scripts
* Data-type validation
* Inconsistent-value checks
* Before/after quality report
* Project documentation

## Task 02

* Exploratory data analysis script
* Statistical analysis reports
* Business statistics
* Sales analysis
* Payment analysis
* Monthly trends
* Review analysis
* Delivery analysis
* Correlation analysis
* Business findings
* Data visualizations

The complete raw and cleaned datasets are maintained separately because of their file size.

---

# Author

**Ameer Hamza**

Data & AI Internship — Task 01 & Task 02
