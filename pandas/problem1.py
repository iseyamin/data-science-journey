import pandas as pd

data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[22,23,21,24,25,22,26],
    "Salary":[48000,33000,35000,42000,25000,30000,41000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}

df = pd.DataFrame(data)
#Print one single column:
column = df["Name"]
print(column)

#Print multiple column
column2 =df[["Name","Salary"]]
print(column2)

#Print conditional rows
row = df[df['Salary']>40000]
#and conditions
row2 = df[(df['Salary']>40000) & (df['Performance']>7)]
print(row)
print(row2)

#Or conditions
row3 = df[(df['Salary']>40000) | (df['Performance']>8)]
print(row3)