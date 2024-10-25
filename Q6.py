import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'dataset.csv'
df = pd.read_csv(dataset_path)

# Count the occurrences of intubation statuses
intubation_counts = df['INTUBATED'].value_counts()

# Plotting the intubation status counts
intubation_counts.plot(kind='bar', color='lightblue', edgecolor='black')

# Adding labels and title
plt.title('Number of Patients Requiring Intubation', fontsize=16)
plt.xlabel('Intubation Status', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
