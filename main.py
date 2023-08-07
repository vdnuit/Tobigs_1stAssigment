import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

numeric_columns = data.select_dtypes(include=[np.number]).columns

plt.figure(figsize=(12, 8))
sns.boxplot(data=data[numeric_columns])
plt.title("Boxplot of Numeric Columns")
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Attrition')
plt.title("Attrition Distribution")
plt.show()

data['WorkingYearsProportion'] = data['TotalWorkingYears']/data['Age'] 

numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
numeric_data = data[numeric_columns]
correlation_matrix = numeric_data.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
