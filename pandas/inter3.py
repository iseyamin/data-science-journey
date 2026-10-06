#time Interpolation

import pandas as pd
data={
    "Area":['Dhaka','Bhola','Bandarban','CoxsBazar', 'Sylhet', 'Rangamati', 'Bhola'],
    "Temperature":[33,23,26,None,25,22,None],
    
}

df = pd.DataFrame(data, index=pd.to_datetime(['2026-01-01','2026-01-02','2026-01-05','2026-01-9','2026-01-10','2026-01-11','2026-01-16']))
print(df)

numeric = df.select_dtypes(include='number').columns
df[numeric] = df[numeric].interpolate(method='time')
# df['Temperature']=df['Temperature'].interpolate(method='time')
print(df)