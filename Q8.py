import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'dataset.csv'
df = pd.read_csv(dataset_path)

# Filter the dataset for deceased patients
deceased_df = df[df['OUTCOME'] == 'DECEASED']

# List of diseases to analyze
diseases = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']

# Count the occurrences of each disease among deceased patients
disease_counts = deceased_df[diseases].apply(lambda x: (x == 1).sum())

# Plot the bar chart for common diseases
disease_counts.plot(kind='bar', color='lightcoral', edgecolor='black')

# Adding labels and title
plt.title('Common Diseases among Deceased Patients', fontsize=16)
plt.xlabel('Disease', fontsize=12)
plt.ylabel('Number of Deceased Patients', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
