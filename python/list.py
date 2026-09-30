marks = [11, 66, 88.9, 'g', "anud"]
print(marks)
print(marks[-1])
print(type(marks) , len(marks))

marks2 = marks[1:3]
print(marks2)

marks2.append("fuck")
marks2.insert(1,55)
print(marks2)

#Touple

cg = (44, 75, 56)
print(cg[2])

#Set=> unoque items

result = {33,65,88,33,66,'a'}
print(result)

#Dictionary data type
mid={"Math":78, "ICT":90, "Physics":77}
print(mid["ICT"])
for i in mid:
    print(i,mid[i])