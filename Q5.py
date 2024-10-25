import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'dataset.csv'
df = pd.read_csv(dataset_path)

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# Cut the 'AGE' column into the defined bins
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels, right=False)

# Group by age group and gender, then count occurrences
age_gender_distribution = df.groupby(['AGE_GROUP', 'SEX']).size().unstack()

# Plotting the distribution by gender and age group
age_gender_distribution.plot(kind='bar', stacked=True, color=['lightblue', 'pink'])

# Adding labels and title
plt.title('Distribution of COVID-19 Cases by Gender and Age Group', fontsize=16)
plt.xlabel('Age Groups', fontsize=12)
plt.ylabel('Number of Cases', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
