print("Unique roll numbers by using list: ")
roll =[101,105,102,101,108,105,110]
roll2 = list(set(roll))
print("Unique roll numbers: ", roll2)



print("Find something by using id: ")

data=[
    (101,"Alica", 50000),
    (102,"Prima",90000),
    (103,"Ritra",45000)
]

for i in data:
    if(102 in i):
        print("Name: "+i[1],"\nSalary: ",i[2])

