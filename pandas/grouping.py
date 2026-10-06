import pandas as pd
data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Eusha','Fariha'],
    "Age":[22,23,22,23,25,24,23],
    "Salary":[48000,33000,42000,25000,29000,41000,36000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}
df = pd.DataFrame(data)

age_group = df.groupby('Age')['Salary'].sum() #single column groupby
age_group2 = df.groupby('Age')['Salary'].count()

nam_age = df.groupby(['Name','Age'])['Salary'].sum() #multiple column groupby

print(age_group)
print(age_group2)
print(nam_age)