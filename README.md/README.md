# Credit Card Analytics Dashboard

An end-to-end data analytics project that explores customer spending behavior, credit card usage, and customer segmentation using SQL, Python, Machine Learning, and Streamlit.

The objective of this project is to analyze customer transaction data, generate business insights, and build an interactive dashboard for data-driven decision making.

---

## Project Overview

This project follows a complete analytics workflow:

- Data Understanding
- Data Cleaning
- Data Integration
- SQL Business Analysis
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Customer Segmentation using K-Means
- Interactive Dashboard Development

---

## Technologies Used

- Python
- PostgreSQL
- SQL
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

---

## Project Structure

```text
credit_card_analytics/

├── cleaned_data/
│   ├── customer_summary.csv
│   ├── customer_segments.csv
│   ├── master_dataset.csv
│   └── ...
│
├── dashboard/
│   ├── app.py
│   └── requirements.txt
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_master_dataset.ipynb
│   ├── 04_eda.ipynb
│   ├── 05_feature_engineering.ipynb
│   └── 06_customer_segmentation.ipynb
│
├── sql/
│   ├── queries_01.sql
│   ├── queries_02.sql
│   └── queries_03.sql
│
├── data/
├── images/
├── README.md
├── LICENSE
└── .gitignore
```

---

# Workflow

## 1. Data Cleaning

The raw datasets were examined for missing values, incorrect data types, and inconsistencies. Cleaned datasets were exported for further analysis.

---

## 2. Data Integration

Customer, card, and transaction datasets were merged to create a unified master dataset for analysis.

---

## 3. SQL Business Analysis

Several business-oriented SQL queries were written using PostgreSQL, including:

- Top spending customers
- Monthly revenue analysis
- State-wise spending trends
- Customer ranking
- Card usage analysis
- Common Table Expressions (CTEs)
- Window Functions
- Ranking Functions
- Aggregate Analysis

---

## 4. Exploratory Data Analysis

EDA was performed to understand customer behavior through visualizations, including:

- Customer Segment Distribution
- Income Distribution
- Credit Limit Distribution
- Revenue by State
- Revenue by Occupation
- Payment Method Analysis
- Monthly Revenue Trends

---

## 5. Feature Engineering

Customer-level features were created to improve analysis and customer profiling.

Features include:

- Total Spending
- Average Transaction Amount
- Maximum Transaction
- Total Transactions
- Cards Owned
- Spending-to-Income Ratio
- Customer Lifetime
- Average Spend Per Day
- High Value Customer Flag

---

## 6. Customer Segmentation

K-Means Clustering was applied to group customers based on their financial behavior.

Features used:

- Annual Income
- Total Spending
- Average Transaction
- Cards Owned
- Spending-to-Income Ratio
- Average Spend Per Day

---

## 7. Interactive Dashboard

A Streamlit dashboard was developed to present the analysis interactively.

The dashboard includes:

- Overview KPIs
- Customer Segment Analysis
- High Value Customer Analysis
- Income vs Spending Visualization
- Cluster Distribution
- Cluster Summary
- Top Customers
- Customer Dataset Viewer

---

# Dashboard Preview

## Dashboard

(Add dashboard screenshot here)

```
images/dashboard.png
```

---

# Key Insights

- Standard customers form the largest customer segment.
- High-value customers contribute significantly to total spending.
- Customer segmentation identifies groups with distinct spending patterns.
- Spending-to-income ratio provides additional insight into customer purchasing behavior.

---
## Dashboard Preview

### Dashboard Overview

![Dashboard Overview](images/dashboard1.png)

![Customer Segmentation](images/dashboard2.png)

![Cluster Analysis](images/dashboard3.png)

# How to Run

Clone the repository

```bash
git clone <repository_url>
```

Install the required packages

```bash
pip install -r dashboard/requirements.txt
```

Run the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

---

# Learning Outcomes

This project provided practical experience in:

- Writing business-oriented SQL queries
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Customer Segmentation using Machine Learning
- Building interactive dashboards using Streamlit

---

# Future Improvements

- Merchant-level analytics
- Interactive filtering across all charts
- Dashboard deployment on Streamlit Community Cloud
- Predictive customer analytics
- Additional customer behavior metrics

---

## Made By

**Ritika Sharma**

Electronics and Communication Engineering Student

Interested in Data Analytics, Software Development, and Machine Learning.