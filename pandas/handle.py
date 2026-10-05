
import pandas as pd

data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[22,23,None,24,25,22,26],
    "Salary":[48000,33000,None,42000,25000,None,41000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}

df =pd.DataFrame(data)
print(df)

#By removing missing data
# df.dropna(inplace=True) #all missing values rows will remove
# print(df)

#Add default value 
# df.fillna(0,inplace=True)  # .fillna(value, inplace=TRue)
# print(df)

#Full with conditional values
df['Age'] = df['Age'].fillna(df['Age'].mean()) #Age column fill with average value
#df['Age'] = df['Age'].fillna(int(df['Age'].mean())) #if we need integer value
df["Salary"] = df['Salary'].fillna(df['Salary'].mean())
print(df)