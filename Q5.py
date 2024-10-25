import pandas as pd
import matplotlib.pyplot as plt

# Load the transformed data
df = pd.read_csv('transformed_data.csv')

# Convert "SEX" to categorical values explicitly
df['SEX'] = df['SEX'].astype('category')

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = [f'{age_bins[i]}-{age_bins[i+1]}' for i in range(len(age_bins)-1)]
df['age_group'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels)

# Create the pivot table for age groups and gender
age_gender_distribution = pd.pivot_table(df, index='age_group', columns='SEX', aggfunc='size', fill_value=0)

# Plot the distribution by gender and age group
age_gender_distribution.plot(kind='bar', stacked=True)
plt.title('Distribution of COVID-19 Cases by Gender and Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.show()