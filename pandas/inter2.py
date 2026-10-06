#Index Interpolation

import pandas as pd
data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[None,23,26,24,25,22,None],
    "Salary":[48000,33000,42000,25000,None,41000,None],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}
df = pd.DataFrame(data, index=[1,2,3,4,7,8,9])
print(df)

numeric = df.select_dtypes(include='number').columns
df[numeric] = df[numeric].interpolate(method='index')
print(df)