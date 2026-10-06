import pandas as pd
data1={
    "Name":['Sadia','Lamia','Eusha','Anud','Adhara','Eusha','Fariha'],
    "ID": [757,453,605,660,893,297,326],
    "Age":[22,23,22,24,25,24,23],
    "Salary":[48000,33000,42000,25000,29000,41000,36000],
    "Performance":[8.2,8.6,7.7,5.6,7.9,8.0,7.2]
}
df1 = pd.DataFrame(data1)

data2={

    "ID": [453,297,575,757,600,893,289,321],
    "cgpa":[3.55, 2.97, 3.22, 4.00, 3.85, 3.24, 3.63,3.33]
}
df2 = pd.DataFrame(data2)

new = pd.concat([df1,df2], axis=1) #add horizontally -> column wise
new2 = pd.concat([df1,df2], axis=0) #add vertically -> row wise
print(new)
print(new2)