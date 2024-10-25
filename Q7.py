import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'dataset.csv'
df = pd.read_csv(dataset_path)

# List of diseases and ICU status
diseases = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']
df_diseases_icu = df[diseases + ['ICU']]

# Convert all columns to numeric to handle categorical data properly
df_diseases_icu = df_diseases_icu.apply(pd.to_numeric, errors='coerce')

# Calculate the correlation matrix
correlation_matrix = df_diseases_icu.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Adding labels and title
plt.title('Correlation between Diseases and ICU Admission', fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Show the plot
plt.tight_layout()
plt.show()
