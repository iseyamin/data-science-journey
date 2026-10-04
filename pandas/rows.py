import pandas as pd

#Read data from CSV file
df = pd.read_excel(r"E:\8th semester\data-science-journey\pandas\SampleSuperstore.xlsx")
print("First 4 lines of data:")
print(df.head(4))