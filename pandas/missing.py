import pandas as pd

data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[22,23,None,24,25,22,26],
    "Salary":[48000,33000,None,42000,25000,30000,41000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}

df =pd.DataFrame(data)
print(df)
print(df.isnull()) #Show the boolean output. missing value-> True
print(df.isnull().sum()) #count how many null in each column