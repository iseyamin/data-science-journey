print("Problem 1: ")
i=1
while i<=100:
    if(i%2 != 0):
        print(i )
    i+=1

print("Problem 3: ")
for i in range(1,50,1):
    if(i==15):
        continue
    elif(i%3==0):
        print(i)

print("Problem 4: ")
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

for i in range(1,1000,1):
    if(i%a==0) and (i%b==0):
        print("lucky number = ", i)
        break
    
print("End loop")