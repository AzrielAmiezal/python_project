import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset and data dictionary
dataset_path = 'dataset.csv'
data_dictionary_path = 'data_dictionary.xlsx'

# Load the dataset
df = pd.read_csv(dataset_path)

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# Cut the 'AGE' column into the defined bins
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels, right=False)

# Count the occurrences in each age group
age_group_counts = df['AGE_GROUP'].value_counts().sort_index()

# Plotting the bar chart based on age group counts from Question 2
plt.figure(figsize=(10, 6))
age_group_counts.plot(kind='bar', color='skyblue')

# Adding labels and title
plt.title('COVID-19 Susceptibility by Age Group', fontsize=16)
plt.xlabel('Age Groups', fontsize=12)
plt.ylabel('Number of Cases', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
