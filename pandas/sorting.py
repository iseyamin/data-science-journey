import pandas as pd
data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Eusha','Fariha'],
    "Age":[22,23,22,24,25,24,23],
    "Salary":[48000,33000,42000,25000,29000,41000,36000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}
df = pd.DataFrame(data)

# df.sort_values(by='Name',ascending=True,inplace=True) #Sorting by one column

df.sort_values(by=['Name','Age'],ascending=[True,False],inplace=True) #sorting by multiple columns
print(df)