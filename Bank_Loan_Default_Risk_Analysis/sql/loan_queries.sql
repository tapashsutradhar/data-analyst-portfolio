-- Total number of loans
SELECT COUNT(*) AS total_loans FROM bank_loans;

-- Loan approval vs rejection
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

-- Cluster segmentation (from ML)
SELECT Cluster, COUNT(*) AS customers,
       AVG(TotalIncome) AS avg_income,
       AVG(LoanAmount) AS avg_loan,
       AVG(DTI) AS avg_dti
FROM bank_loans
GROUP BY Cluster;

-- Property area vs default
SELECT Property_Area, Loan_Status, COUNT(*) AS total
FROM bank_loans
GROUP BY Property_Area, Loan_Status;
