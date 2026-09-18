# Olist E-Commerce Data & AI Project

A data cleaning and quality-checking project based on the Olist Brazilian E-Commerce Public Dataset.

This project was completed as part of a Data & AI Internship Task 01. The main objective was to inspect the datasets, identify data-quality problems, clean the data, validate data types and values, and generate a before/after quality report.

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

The original dataset files are not included in this public repository because of their large size. They were kept locally during the cleaning process.

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

## Before / After Summary

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

## Project Structure

```text
Olist-Ecommerce-Data-AI-Project/
│
├── reports/
│   └── task01_before_after_report.csv
│
├── src/
│   ├── clean_dataset.py
│   ├── task01_quality_check.py
│   ├── task01_datatypes_check.py
│   ├── task01_inconsistent_check.py
│   ├── task01_problem_records.py
│   └── task01_report.py
│
├── .gitignore
└── README.md
```

## Tools & Technologies

* Python
* Pandas
* NumPy
* CSV
* Git
* GitHub

## Task 01 Deliverables

This repository contains:

* Python data-cleaning scripts
* Data-quality checking scripts
* Data-type validation
* Inconsistent-value checks
* Before/after quality report
* Project documentation

The complete raw and cleaned datasets are maintained separately because of their file size.

## Author

**Nexora Labs**

Data & AI Internship — Task 01
