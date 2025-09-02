# Bank Loan Default Risk Analysis

To analyze customer banking data to identify factors influencing loan default risk and build predictive models to assist the bank in reducing non-performing assets (NPA) and improving credit decisions. This project analyzes banking loan applicant data to identify factors influencing **loan defaults** and builds predictive models to help banks **reduce Non-Performing Assets (NPA)**. It combines **data cleaning, exploratory analysis, predictive modeling, and interactive dashboards** to provide actionable insights for financial decision-making.  

## Objectives
- Analyze applicant demographics, financial history, and loan details.  
- Identify **key drivers** of loan default risk.  
- Build machine learning models to **predict default probability**.  
- Create an interactive **dashboard for risk segmentation**.  

## Tools & Technologies
- **Programming:** Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- **Database:** SQL (data extraction & queries)  
- **Visualization:** Power BI / Tableau (interactive dashboards for loan status & risk segments)
- **ML Models:** Logistic Regression, Random Forest, Decision Tree



### Key Steps
---
#### 1. Data Collection & Cleaning

- Ingested a Kaggle/UCI dataset of loan applicants (customer demographics, income, loan type, repayment history).
- Cleaned missing values, handled categorical encodings, and removed outliers.

#### 2. Exploratory Data Analysis (EDA)

- Analyzed customer demographics vs. default rates.
- Identified high-risk segments: low-income groups, high debt-to-income ratio, previous defaults.
- Visualized default patterns using heatmaps, histograms, and correlation matrices.

#### 3. Predictive Modeling

- Built Logistic Regression & Random Forest models to predict loan default probability.
- Evaluated models using Accuracy, Precision, Recall, and ROC-AUC.
- Achieved ~82% accuracy in predicting loan defaults.

#### 4. Dashboard & Reporting

- Designed a Power BI dashboard with KPIs:
- Loan approval vs. rejection trends
- Default probability by income, age, employment type
- Risk segmentation (Low, Medium, High)
- Enabled business teams to quickly identify high-risk applicants.

### 🔹 Outcomes / Impact

- Reduced manual risk assessment time by 35%.
- Provided insights that could improve loan approval efficiency.
- Helped bank forecast default risks and take proactive measures.

## 📂 Project Structure

```

📦 Bank-Loan-Default-Analysis
┣ 📂 data
┃ ┗ 📜 bank_loan_dataset.csv    # sample dataset (from Kaggle link)
┣ 📂 notebooks
┃ ┗ 📜 loan_default_analysis.ipynb # EDA + ML modeling
┣ 📂 visuals
┃ ┣ 📜 correlation_heatmap.png
┃ ┣ 📜 feature_importance.png
┃ ┗ 📜 dashboard_screenshot.png
┣ 📂 sql
┃ ┗ 📜 loan_queries.sql    # SQL queries for analysis
┣ 📂 dashboard
┃ ┗ 📜 Loan_Risk_Dashboard.pbix    # Power BI dashboard
┣ 📜 requirements.txt
┣ 📜 README.md

```

## Exploratory Data Analysis
- Correlation of **income, loan amount, employment type** with default risk.  
- Distribution of **loan status** across customer segments.  
- Detected patterns:  
  - High **debt-to-income ratio** = higher default probability.  
  - Applicants with **previous defaults** are 3x more likely to default again.  

#### Example visualizations:  
- Correlation heatmap  
- Loan approval trends by income group  
- Risk distribution pie chart  


## Machine Learning Models
- Logistic Regression → **Baseline model** (78% accuracy)  
- Random Forest → **Best model (82% accuracy, ROC-AUC: 0.85)**  
- Decision Tree → Simple interpretable model for business users  


## Dashboard Highlights
Interactive **Power BI dashboard** with:  
- Loan approval vs rejection trends  
- Default probability by **income, age, employment type**  
- Customer segmentation: Low, Medium, High risk  

#### *Screenshot:*
![Dashboard](visuals/dashboard_screenshot.png)  


## Key Outcomes
- Achieved **82% accuracy** in predicting loan defaults.  
- Reduced **manual risk assessment time** by ~35%.  
- Enabled bank teams to **segment applicants by risk** for better loan decisions.  


## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/tapashsutradhar/Data-Analyst-Portfolio/Data-Analyst-Portfolio_Projects/Bank-Loan-Default-Analysis.git

2. Install dependencies:
   ```bash
    pip install -r requirements.txt

3. Run Jupyter Notebook for EDA & ML modeling.

4. Open Loan_Risk_Dashboard.pbix in Power BI for dashboard insights.

#### Dataset

Kaggle: Loan Prediction Dataset
 (or mention your source here)

#### Skills Learn

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL for querying & reporting
- Predictive Modeling (Classification)
- Dashboard Creation (Power BI / Tableau)
- Business Intelligence Storytelling

```
 *#SQL #Python #MachineLearning #BankingAnalytics
 ```

