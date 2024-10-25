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

print(age_group_counts)
