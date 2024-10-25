import pandas as pd


#import data
df = pd.read_csv("dataset.csv")

#view dataframe
print(df.head(10))

# dataframe info
print(df.info())

# change format date from object to datetime
df["ADMISSION DATE"] = pd.to_datetime(df["ADMISSION DATE"])

df["DATE_OF_FIRST_SYMPTOM"] = pd.to_datetime(df["DATE_OF_FIRST_SYMPTOM"])

df["DATE_OF_DEATH"] = pd.to_datetime(df["DATE_OF_DEATH"])

df.info()

print(df)

# import dictionary data
data = pd.read_excel("data_dictionary.xlsx")

print(data)

data['variable'] = data['variable'].str.upper()

def parse(value_string):
    return {
        int(key.strip()): value.strip()
        for item in value_string.split(",")
        for key, value in [item.split("=")]
    }

# Create a dictionary for each 'variable' based on the parsed 'value'
data_dict = {
    row['variable']: parse(row['value'])
    for _, row in data.iterrows()
}

# Print the result
print(data_dict)

for col in df.columns:
    if col in data_dict:  # Check if the column has a corresponding dictionary
        df[col] = df[col].map(data_dict[col])  # Map values

print(df)

# Define age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# Cut the 'AGE' column into the defined bins
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=age_bins, labels=age_labels, right=False)

# Count the occurrences in each age group
age_group_counts = df['AGE_GROUP'].value_counts().sort_index()

print(age_group_counts)

print(df.head(10))

df.to_csv("dataset_cleaned.csv", index=False)