from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV beside this script, regardless of the terminal's working directory.
data_path = Path(__file__).resolve().parent / 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(data_path)
# Blank TotalCharges values represent missing data, not zero charges.
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# 1. Feature Engineering: Convert Churn to binary (0 or 1) for statistical math
df['Churn_Value'] = df['Churn'].map({'Yes': 1, 'No': 0})

# 2. Programmatic Insight: Churn Rate by Payment Method
# Calculate rates directly from the loaded data.
print("--- Churn Rate by Payment Method (%) ---")
payment_churn = df.groupby('PaymentMethod')['Churn_Value'].mean() * 100
print(payment_churn.sort_values(ascending=False).round(2))
print("\n")

# 3. Programmatic Insight: Churn Rate by Contract Type
print("--- Churn Rate by Contract Type (%) ---")
contract_churn = df.groupby('Contract')['Churn_Value'].mean() * 100
print(contract_churn.sort_values(ascending=False).round(2))
print("\n")

# 4. Advanced Analyst Skill: Statistical Correlation Heatmap
# Measure numeric associations; correlation does not establish causation.
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn_Value']
correlation_matrix = df[numeric_cols].corr()

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix: Numeric Features vs. Churn')
plt.tight_layout()
plt.show()

print("Heatmap generated successfully.")
