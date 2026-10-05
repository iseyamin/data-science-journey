import pandas as pd

data={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Erin','Fariha'],
    "Age":[22,23,21,24,25,22,26],
    "Salary":[48000,33000,35000,42000,25000,30000,41000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}

df = pd.DataFrame(data)

df["Bonus"]=df["Salary"]*0.1
print(df)

#Using insert method for specific position
df.insert(0,"Employee ID",[1,2,4,7,22,13,21]) #df.insert(location/index, "column_name",[values])
print(df)

#Update value-> df.loc[row_index,"column_name"]=new value
df.loc[2,"Salary"]=36000
print(df)


#delete column
df.drop(columns=["Employee ID"], inplace=True)
#df.drop(columns=["Employee ID","Age"], inplace=True)  #for delete multiple column
print(df)