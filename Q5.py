import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset and data dictionary
dataset_path = 'dataset.csv'
data_dictionary_path = 'data_dictionary.xlsx'

# Load the transformed data
df = pd.read_csv(dataset_path)

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = [f'{age_bins[i]}-{age_bins[i+1]}' for i in range(len(age_bins)-1)]

# Create age groups
df['age_group'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels)

# Create a pivot table for age groups and gender
age_gender_distribution = pd.p
