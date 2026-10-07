import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\8th semester\data-science-journey\pandas\Mini Project\laptopData.csv")
#print(df.tail())

#check missing values
# print(df.isnull().sum())
#Remove missing values rows, because company name, Type name is missing too
df.dropna(inplace=True)
#Remove duplicate records
df.drop_duplicates(inplace=True)

#replace negative price
df['Price'] = np.where(df['Price']<0, df['Price'].mean(), df['Price']) #(condition, if true, if false)

price_mean = df['Price'].mean()
price_std = df['Price'].std()
lower_bound = price_mean-(4*price_std)
upper_bound = price_mean+(4*price_std)
#Filtering rows
df = df[(df['Price']>lower_bound) & (df['Price']<upper_bound)]
#Adding profit column
df["Profit"] = df['Price']*0.1
#Sorting by brand name
df.sort_values(by=['Company','TypeName'], ascending=[True,True], inplace=True)
#delete unnamed0 column
df = df.drop(columns="Unnamed: 0")
#print(df.head())

#All brand profit table
# GroupByBrand = df.groupby('Company')['Profit'].sum()
GroupByBrand = df.groupby('Company').agg(
    Total_Profit=('Profit','sum'),
    Sale_Count =('Profit','count')).reset_index()
GroupByBrand.sort_values(by='Total_Profit', ascending=False, inplace=True)
#print(GroupByBrand)

#Save csv file
df.to_csv("Clean_SalesReport.csv",index=False)
GroupByBrand.to_csv("Company_Profit.csv",index=False)
