
# Olist E-Commerce Data & AI Project

A data analysis project based on the Olist Brazilian E-Commerce Public Dataset. This project covers data cleaning, exploratory data analysis, business insights, data visualization, and SQL analysis.

**Author:** Ameer Hamza  
**Project:** Data & AI Internship

## Project Overview

This project analyzes e-commerce data to understand order performance, payment methods, product categories, customer reviews, pricing, freight charges, and delivery performance.

The project is organized into four tasks.

## Project Tasks

| Task | Description | Main Deliverable |
|---|---|---|
| Task 01 | Data Cleaning & Quality Checking | Cleaned datasets and quality reports |
| Task 02 | Exploratory Data Analysis | Statistical reports and business insights |
| Task 03 | Data Visualization | Charts and visual reports |
| Task 04 | SQL Data Analysis | SQL queries, database documentation, and query results |

## Task 01 — Data Cleaning & Quality Checking

### Objectives

- Load datasets using Python and Pandas.
- Identify missing values and duplicate records.
- Check incorrect and inconsistent values.
- Validate data types.
- Prepare cleaned datasets.
- Generate data-quality reports.

### Dataset

The project uses nine datasets:

1. Customers
2. Geolocation
3. Orders
4. Order Items
5. Order Payments
6. Order Reviews
7. Products
8. Sellers
9. Product Category Translation

### Cleaning Summary

| Dataset | Rows After Cleaning |
|---|---:|
| Customers | 99,441 |
| Geolocation | 738,332 |
| Orders | 99,441 |
| Order Items | 112,650 |
| Order Payments | 103,886 |
| Order Reviews | 99,224 |
| Products | 32,951 |
| Sellers | 3,095 |
| Category Translation | 71 |

The main duplicate issue was identified in the geolocation dataset. Missing values, data types, and inconsistent values were also checked.

### Task 01 Files

- `src/clean_dataset.py`
- `src/task01_quality_check.py`
- `src/task01_datatypes_check.py`
- `src/task01_inconsistent_check.py`
- `src/task01_problem_records.py`
- `src/task01_report.py`
- `reports/task01_before_after_report.csv`

## Task 02 — Exploratory Data Analysis & Business Insights

### Objectives

- Calculate business statistics.
- Analyze sales and product categories.
- Examine payment methods.
- Analyze monthly order and sales trends.
- Study review scores and delivery times.
- Explore product prices and freight charges.
- Examine relationships between numerical variables.
- Document business findings.

### Reports

The Task 02 reports are stored in:

- `reports/task02/statistics/`
- `reports/task02/findings/task02_important_findings.txt`
- `reports/task02/visualizations/`

The statistical reports cover business statistics, delivery times, monthly trends, payment methods, product statistics, correlations, review scores, and sales by category.

### Main Script

`src/task02_analysis.py`

## Task 03 — Build Data Visualizations

### Objectives

Create charts that communicate important business patterns and trends.

### Visualizations

1. Top product categories by sales
2. Monthly order trend
3. Payment methods
4. Delivery time distribution
5. Product price versus freight value
6. Customer review score distribution
7. Payment value by method

### Files

- Python script: `src/task03_visualizations.py`
- Charts folder: `reports/task03/visualizations/`

### Run Task 03

From the project root directory:

```bash
python src/task03_visualizations.py
```

The generated charts are saved in `reports/task03/visualizations/`.

## Task 04 — Perform SQL Data Analysis

### Objectives

- Create an SQLite database from cleaned CSV files.
- Import datasets into database tables.
- Query data using SELECT and WHERE.
- Summarize data using GROUP BY and aggregate functions.
- Combine related tables using JOIN.
- Analyze order statuses, payment methods, product categories, review scores, and customer locations.

### SQL Analysis

The project includes eight SQL queries covering:

1. Sample customer records
2. Delivered orders
3. Order status counts
4. Payment method summaries
5. Orders joined with customer information
6. Product categories and category translations
7. Average customer review score
8. Orders by customer state

### Task 04 Files

- Database import script: `src/task04/import_database.py`
- SQL queries: `src/task04/queries.sql`
- Query execution script: `src/task04/run_queries.py`
- Database table report script: `src/task04/table_report.py`
- Database documentation: `reports/task04/database_tables.md`
- Query results: `reports/task04/query_results.txt`

### Key Findings

- Total orders analyzed: 99,441
- Delivered orders: 96,478
- Average customer review score: 4.09 out of 5
- Credit card was the most frequently recorded payment method.
- São Paulo (SP) had the highest number of orders among the states analyzed.

### Run Task 04

Run the database import script first, after preparing the cleaned datasets and installing the required dependencies. Then execute the SQL query runner.

```bash
python src/task04/import_database.py
python src/task04/run_queries.py
```

The database is generated locally and is excluded from Git because of its size. The import script can recreate it when the cleaned datasets are available.

## Project Structure

```text
Olist-Ecommerce-Data-AI-Project/
├── reports/
│   ├── task01_before_after_report.csv
│   ├── task02/
│   │   ├── findings/
│   │   ├── statistics/
│   │   └── visualizations/
│   ├── task03/
│   │   └── visualizations/
│   └── task04/
│       ├── database_tables.md
│       └── query_results.txt
├── src/
│   ├── clean_dataset.py
│   ├── task01_quality_check.py
│   ├── task01_datatypes_check.py
│   ├── task01_inconsistent_check.py
│   ├── task01_problem_records.py
│   ├── task01_report.py
│   ├── task02_analysis.py
│   ├── task03_visualizations.py
│   └── task04/
│       ├── import_database.py
│       ├── queries.sql
│       ├── run_queries.py
│       └── table_report.py
├── .gitignore
└── README.md
```

*Note: This is the main project structure. Additional files may exist locally. The original and cleaned datasets are not included in the repository.*

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- CSV
- Git
- GitHub

## Project Deliverables

- Data cleaning and quality-checking scripts
- Cleaned datasets and data-quality reports
- Exploratory data analysis
- Statistical summaries and business insights
- Seven data visualizations for Task 03
- SQL queries and SQLite database creation scripts
- Database documentation and query results

## Repository

[View the complete project on GitHub](https://github.com/Ameer779/Olist-Ecommerce-Data-AI-Project)

## Author

**Ameer Hamza**

Data & AI Internship — Tasks 01, 02, 03, and 04
