"""
ETL + ML Pipeline for Bank Loan Default Analysis
------------------------------------------------
1. Extract raw data from Kaggle dataset
2. Transform: clean, feature engineering (TotalIncome, DTI, EMI)
3. Train Logistic Regression model for default prediction
4. Load: Save processed data + predictions to CSV & SQLite
5. Save reusable SQL queries
"""

import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

# Encode categorical variables
df_encoded = df.copy()
le = LabelEncoder()
for col in df_encoded.select_dtypes(include=["object"]).columns:
    df_encoded[col] = le.fit_transform(df_encoded[col])

# ==============================
# 4. Predictive Model
# ==============================
print("Training predictive model...")

if "Loan_Status" in df_encoded.columns:
    X = df_encoded.drop("Loan_Status", axis=1)
    y = df_encoded["Loan_Status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model trained: Accuracy = {acc:.2f}")

    # Add predictions back to df
    df["Default_Prob"] = model.predict_proba(X)[:, 1]
    df["High_Risk"] = (df["Default_Prob"] > 0.5).astype(int)
else:
    print("Loan_Status column not found — skipping model step")

# ==============================
# 5. Load
# ==============================
print("Saving outputs...")

# Save processed CSV
df.to_csv(PROCESSED_CSV, index=False)
print(f"Processed CSV saved: {PROCESSED_CSV}")

# Save into SQLite DB
conn = sqlite3.connect(SQLITE_DB)
df.to_sql("bank_loans", conn, if_exists="replace", index=False)
conn.close()
print(f"Data with predictions loaded into SQLite DB: {SQLITE_DB}")

# Save SQL queries file
queries = """-- Loan Default Analysis Queries with Predictions

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

-- High risk customers (from ML model)
SELECT Loan_ID, ApplicantIncome, LoanAmount, Default_Prob, High_Risk
FROM bank_loans
WHERE High_Risk = 1
ORDER BY Default_Prob DESC
LIMIT 20;

-- Property area vs default
SELECT Property_Area, Loan_Status, COUNT(*) AS total
FROM bank_loans
GROUP BY Property_Area, Loan_Status;
"""
SQL_QUERIES.write_text(queries)
print(f"SQL queries saved: {SQL_QUERIES}")
