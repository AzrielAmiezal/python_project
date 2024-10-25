#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px

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

data = pd.read_excel("data_dictionary.xlsx")

data

data['variable'] = data['variable'].str.upper()

def parse_value_string(value_string):
    return {
        int(key.strip()): value.strip()
        for item in value_string.split(",")
        for key, value in [item.split("=")]
    }

# Create a dictionary for each 'variable' based on the parsed 'value'
data_dict = {
    row['variable']: parse_value_string(row['value'])
    for _, row in data.iterrows()
}

# Print the result
print(data_dict)

for col in df.columns:
    if col in data_dict:  # Check if the column has a corresponding dictionary
        df[col] = df[col].map(data_dict[col])  # Map values

print(df)