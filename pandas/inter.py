#Interpolation

import pandas as pd
data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[None,23,26,24,25,22,None],
    "Salary":[48000,33000,42000,25000,None,41000,None],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}
df = pd.DataFrame(data)
#applying linear interpolation
#forward -> analysis past data
#backward -> analysis future data
#both -> analysis both data

#df['Age'] = df['Age'].interpolate(method='linear',limit_direction='forward') #for single column
numeric = df.select_dtypes(include='number').columns #For applying full dataset, define a variable where include all number columns
df[numeric] = df[numeric].interpolate(method='linear',limit_direction='backward')
print(df)
