# Importing necessary libraries
import pandas as pd
import numpy as np 

from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#load dataset
df = pd.read_csv(r'c:\Users\Nikhi\OneDrive\Desktop\WaterQualityPred\Water_Quality_Pred\dataset.csv', sep=';')
print (df)

#Information about the dataset
print(df.info())

#r Rows and columns
print(df.shape)

# Stats of dataset
print(df.describe().T)

# Check for Missing values
print(df.isnull().sum())

# date is in datetime format
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
print(df.info())

# Short dataset

df = df.sort_values(by= ['id', 'date'])
print(df.head())

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
print(df.head())

print(df.columns)

# Pollutants

pollutants = [ 'O2','NO3','NO2','NH4','SO4','PO4','CL','NH3']
print(pollutants)
