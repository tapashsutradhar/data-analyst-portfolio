"""
ETL Pipeline for Bank Loan Default Analysis
-------------------------------------------
- Extract raw data from Kaggle dataset
- Transform: clean, handle missing values, feature engineering (TotalIncome, DTI, EMI)
- Load: Save to processed CSV + SQLite database
"""

import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path

# ==============================
# 1. Paths
# ==============================
RAW_DATA = Path("data/bank_loan_dataset.csv")
PROCESSED_CSV = Path("data/processed_bank_loan.csv")
SQLITE_DB = Path("data/bank_loan_analysis.db")
SQL_QUERIES = Path("sql/loan_queries.sql")

# ==============================
# 2. Extract
# ==============================
print("Extracting raw dataset...")
df = pd.read_csv(RAW_DATA)

# ==============================
# 3. Transform
# ==============================
print("Transforming dataset...")

# Drop obvious ID column
for id_col in ["Loan_ID", "loan_id", "ID", "id"]:
    if id_col in df.columns:
        df = df.drop(columns=[id_col])

# Fill missing values
for col in df.columns:
    if df[col].dtype.kind in "biufc":  # numeric
        df[col] = df[col].fillna(df[col].median())
    else:  # categorical
        mode_val = df[col].mode(dropna=True)
        if len(mode_val) > 0:
            df[col] = df[col].fillna(mode_val.iloc[0])
        else:
            df[col] = df[col].fillna("Unknown")

# Feature engineering
if {"ApplicantIncome", "CoapplicantIncome"}.issubset(df.columns):
    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

if {"LoanAmount", "Loan_Amount_Term"}.issubset(df.columns):
    df["EMI"] = df["LoanAmount"] / df["Loan_Amount_Term"].replace(0, np.nan)

if {"LoanAmount", "TotalIncome"}.issubset(df.columns):
    df["DTI"] = df["LoanAmount"] / df["TotalIncome"].replace(0, np.nan)

# ==============================
# 4. Load
# ==============================

# Save processed CSV
df.to_csv(PROCESSED_CSV, index=False)
print(f"Processed CSV saved: {PROCESSED_CSV}")

# Save into SQLite DB
conn = sqlite3.connect(SQLITE_DB)
df.to_sql("bank_loans", conn, if_exists="replace", index=False)
conn.close()
print(f"Data loaded into SQLite DB: {SQLITE_DB}")

# Save SQL queries file
queries = """-- Loan Default Analysis Queries

-- Total number of loans
SELECT COUNT(*) AS total_loans FROM bank_loans;

-- Loan approval rate
SELECT Loan_Status, COUNT(*) AS total
FROM bank_loans
GROUP BY Loan_Status;

-- Average income of defaulters vs non-defaulters
SELECT Loan_Status, AVG(TotalIncome) AS avg_income
FROM bank_loans
GROUP BY Loan_Status;

-- Risk segmentation by DTI
SELECT 
    CASE 
        WHEN DTI < 0.2 THEN 'Low Risk'
        WHEN DTI BETWEEN 0.2 AND 0.4 THEN 'Medium Risk'
        ELSE 'High Risk'
    END AS risk_category,
    COUNT(*) AS applicants
FROM bank_loans
GROUP BY risk_category;

-- Gender bias check
SELECT Gender, Loan_Status, COUNT(*) AS total
FROM bank_loans
GROUP BY Gender, Loan_Status;

-- Property area vs default
SELECT Property_Area, Loan_Status, COUNT(*) AS total
FROM bank_loans
GROUP BY Property_Area, Loan_Status;
"""
SQL_QUERIES.write_text(queries)
print(f"SQL queries saved: {SQL_QUERIES}")
