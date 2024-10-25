import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and data dictionary
dataset_path = 'dataset.csv'
data_dictionary_path = 'data_dictionary.xlsx'

# Load the dataset
df = pd.read_csv(dataset_path)

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(df['AGE'], bins=age_bins, edgecolor='black', color='lightblue')

# Adding labels and title
plt.title('COVID-19 Susceptibility by Age Group (Histogram)', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Number of Cases', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
