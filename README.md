# Olist E-Commerce Data & AI Project

A data analysis and AI-focused project based on the Olist Brazilian E-Commerce Public Dataset.

This project is being completed as part of a Data & AI Internship. It currently includes data cleaning, quality checking, exploratory data analysis, statistical analysis, business insights, and data visualization.

## Project Overview

The project analyzes the Olist Brazilian E-Commerce Public Dataset to understand data quality, business performance, sales trends, payment methods, customer reviews, product categories, pricing, freight, and delivery performance.

The project is divided into the following tasks:

- **Task 01:** Data Cleaning & Quality Checking
- **Task 02:** Exploratory Data Analysis & Business Insights
- **Task 03:** Build Data Visualizations

---

# Task 01 — Data Cleaning & Quality Checking

## Task 01 Objectives

- Load datasets using Python and Pandas.
- Identify missing values.
- Check and remove duplicate records where appropriate.
- Handle incorrect or inconsistent values.
- Validate and correct data types where necessary.
- Export cleaned datasets.
- Generate a before-and-after data-quality report.

## Dataset

The project uses the Olist Brazilian E-Commerce Public Dataset containing nine CSV datasets:

1. Customers
2. Geolocation
3. Orders
4. Order Items
5. Order Payments
6. Order Reviews
7. Products
8. Sellers
9. Product Category Translation

The original dataset files are not included in this public repository because of their size. They were maintained locally during the analysis process.

## Data Cleaning Performed

### Missing Values

Missing values were identified in the Orders, Reviews, and Products datasets.

- Missing review titles were replaced with `No title`.
- Missing review messages were replaced with `No review message`.
- Missing product categories were replaced with `Unknown`.
- Missing numerical product values were handled using median values.
- Missing order lifecycle timestamps were retained because they can represent incomplete stages of an order rather than invalid records.

### Duplicate Records

Duplicate records were checked across the datasets.

The main duplicate issue was found in the geolocation dataset:

- Before cleaning: 1,000,163 records
- Duplicate records removed: 261,831
- After cleaning: 738,332 records

### Incorrect and Inconsistent Values

The following checks were performed:

- Negative order item prices
- Negative freight values
- Invalid order item IDs
- Negative payment values
- Invalid payment installments
- Invalid review scores
- Negative product measurements
- Invalid latitude and longitude values
- Order status values
- Order date inconsistencies

Two payment records had zero installments and were corrected to one installment.

Order date inconsistencies were reviewed and retained because they appeared to be timestamp lifecycle issues rather than clear evidence that the complete order records were invalid.

## Task 01 Before / After Summary

| Dataset | Before Rows | After Rows | Rows Removed |
|---|---:|---:|---:|
| Customers | 99,441 | 99,441 | 0 |
| Geolocation | 1,000,163 | 738,332 | 261,831 |
| Orders | 99,441 | 99,441 | 0 |
| Order Items | 112,650 | 112,650 | 0 |
| Order Payments | 103,886 | 103,886 | 0 |
| Order Reviews | 99,224 | 99,224 | 0 |
| Products | 32,951 | 32,951 | 0 |
| Sellers | 3,095 | 3,095 | 0 |
| Category Translation | 71 | 71 | 0 |

---

# Task 02 — Exploratory Data Analysis & Business Insights

## Task 02 Objectives

Task 02 focuses on exploring the cleaned Olist data and generating meaningful statistical and business insights.

The analysis includes:

- Basic statistical analysis
- Sales analysis
- Product category analysis
- Payment method analysis
- Monthly order trends
- Monthly sales trends
- Review score distribution
- Delivery time analysis
- Product price analysis
- Freight analysis
- Correlation analysis
- Identification of important business findings
- Data visualization

## Task 02 Analysis Performed

### Business Statistics

General business statistics were calculated to understand the overall structure and performance of the e-commerce dataset.

### Sales by Product Category

Product categories were analyzed to identify categories with higher sales activity.

### Payment Method Analysis

Payment methods were analyzed to understand customer payment preferences and payment values.

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

`reports/task02/visualizations/`

## Task 02 Statistical Reports

The statistical outputs are stored in:

`reports/task02/statistics/`

The reports include:

- Business statistics
- Delivery time statistics
- Monthly order trend
- Monthly sales trend
- Order items basic statistics
- Payment method analysis
- Payment statistics
- Product statistics
- Relationship correlations
- Review score distribution
- Review statistics
- Sales by product category
- Top 10 highest payment values
- Top 10 highest price items
- Top 10 lowest price items

Important findings are documented in:

`reports/task02/findings/task02_important_findings.txt`

---

# Task 03 — Build Data Visualizations

## Task 03 Objectives

Task 03 focuses on creating clear and meaningful visualizations from the cleaned Olist Brazilian E-Commerce dataset to communicate important business trends and patterns.

The visualizations were generated using Python, Pandas, and Matplotlib.

## Visualizations Created

Seven visualizations were generated for this task.

### 1. Top Product Categories by Sales

**Chart type:** Bar chart

Compares sales values across product categories to identify categories with higher sales activity.

File: `01_top_categories_bar.png`

### 2. Monthly Order Trend

**Chart type:** Line chart

Shows changes in order volume over time and helps identify monthly ordering patterns.

File: `02_monthly_orders_line.png`

### 3. Payment Methods

**Chart type:** Pie chart

Shows the share of payment transactions across different payment methods.

File: `03_payment_methods_pie.png`

### 4. Delivery Time Distribution

**Chart type:** Histogram

Shows the distribution of delivery times in days and helps examine delivery patterns.

File: `04_delivery_time_histogram.png`

### 5. Product Price vs Freight Value

**Chart type:** Scatter plot

Examines the relationship between product prices and freight charges.

File: `05_price_vs_freight_scatter.png`

### 6. Customer Review Score Distribution

**Chart type:** Bar chart

Shows the number of customer reviews for each review score.

File: `06_review_scores_bar.png`

### 7. Payment Value by Method

**Chart type:** Bar chart

Compares total payment values across different payment methods.

File: `07_payment_value_bar.png`

## Task 03 Files

Python visualization script:

`src/task03_visualizations.py`

Generated charts:

`reports/task03/visualizations/`

The script uses cleaned datasets prepared in Task 01 and saves the generated charts as PNG images.

## How to Run Task 03

Run the following command from the project root directory:

```bash
python src/task03_visualizations.py
```

The generated visualizations will be saved in:

`reports/task03/visualizations/`

---

# Project Structure

```text
Olist-Ecommerce-Data-AI-Project/
│
├── reports/
│   ├── task01_before_after_report.csv
│   │
│   ├── task02/
│   │   ├── findings/
│   │   │   └── task02_important_findings.txt
│   │   ├── statistics/
│   │   │   ├── business_statistics.csv
│   │   │   ├── delivery_time_statistics.csv
│   │   │   ├── monthly_order_trend.csv
│   │   │   ├── monthly_sales_trend.csv
│   │   │   ├── order_items_basic_statistics.csv
│   │   │   ├── payment_method_analysis.csv
│   │   │   ├── payments_basic_statistics.csv
│   │   │   ├── products_basic_statistics.csv
│   │   │   ├── relationship_correlations.csv
│   │   │   ├── review_score_distribution.csv
│   │   │   ├── reviews_basic_statistics.csv
│   │   │   ├── sales_by_product_category.csv
│   │   │   ├── top_10_highest_payment_values.csv
│   │   │   ├── top_10_highest_price_items.csv
│   │   │   └── top_10_lowest_price_items.csv
│   │   └── visualizations/
│   │       ├── 01_top_10_product_categories_by_sales.png
│   │       ├── 02_payment_method_analysis.png
│   │       ├── 03_monthly_order_trend.png
│   │       ├── 04_monthly_sales_trend.png
│   │       ├── 05_review_score_distribution.png
│   │       ├── 06_price_vs_freight_relationship.png
│   │       └── 07_delivery_time_distribution.png
│   │
│   └── task03/
│       └── visualizations/
│           ├── 01_top_categories_bar.png
│           ├── 02_monthly_orders_line.png
│           ├── 03_payment_methods_pie.png
│           ├── 04_delivery_time_histogram.png
│           ├── 05_price_vs_freight_scatter.png
│           ├── 06_review_scores_bar.png
│           └── 07_payment_value_bar.png
│
├── src/
│   ├── clean_dataset.py
│   ├── task01_quality_check.py
│   ├── task01_datatypes_check.py
│   ├── task01_inconsistent_check.py
│   ├── task01_problem_records.py
│   ├── task01_report.py
│   ├── task02_analysis.py
│   └── task03_visualizations.py
│
├── .gitignore
└── README.md
```

*Note: The structure lists the main project files and generated reports. Other local files may also exist.*

---

# Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- CSV
- Git
- GitHub
- Data Cleaning
- Data Quality Checking
- Exploratory Data Analysis
- Statistical Analysis
- Data Visualization

---

# Project Deliverables

## Task 01

- Python data-cleaning scripts
- Data-quality checking scripts
- Data-type validation
- Inconsistent-value checks
- Before-and-after quality report
- Project documentation

## Task 02

- Exploratory data analysis script
- Statistical analysis reports
- Business statistics
- Sales analysis
- Payment analysis
- Monthly trends
- Review analysis
- Delivery analysis
- Correlation analysis
- Business findings
- Data visualizations

## Task 03

- Python visualization script
- Seven generated visualizations
- Bar charts
- Line chart
- Pie chart
- Histogram
- Scatter plot
- PNG chart outputs
- Project documentation

The complete raw and cleaned datasets are maintained separately because of their file size.

---

# Author

**Ameer Hamza**

Data & AI Internship — Task 01, Task 02 & Task 03