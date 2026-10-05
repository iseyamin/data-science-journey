import pandas as pd

#Read data from CSV file
df = pd.read_excel(r"E:\8th semester\data-science-journey\pandas\SampleSuperstore.xlsx")
print("First 4 lines of data:")
print(df.head(4))

dff = pd.read_csv(r"E:\8th semester\data-science-journey\pandas\annual-enterprise-survey-2025-financial-year-provisional.csv", encoding="latin1")
print("Last 5 lines of data:")
print(dff.tail())