import pandas as pd

#organize data
data ={
    "Name":["Shakib", "Adib", 'Rayhan'],
    "Age":[26, 22, 24],
    "cgpa":[3.33,3.77,3.22]
}
#store data
df = pd.DataFrame(data)
print(df)

#convert CSV file
#df.to_csv("student.csv")
#df.to_csv("student.csv",index=False) #for remove index number
df.to_excel("student.xlsx",index=False) #for remove index number