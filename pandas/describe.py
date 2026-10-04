import pandas as pd

data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[22,23,21,24,25,22,26],
    "Salary":[48000,33000,35000,42000,25000,30000,41000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}

df = pd.DataFrame(data)
print("Sample data Frame:")
print(df)
print("Descriptive staticstics:")
print(df.describe())