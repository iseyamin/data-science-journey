import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E:\8th semester\data-science-journey\project1\Student Performance Data Analysis (Responses) - Form Responses 1.csv")
print(df.head())
print(df.info()) #check datatype and missing values of every column
print(df.describe())
# Display column names
print(df.columns.tolist())
# Number of rows and columns
print(df.shape)



