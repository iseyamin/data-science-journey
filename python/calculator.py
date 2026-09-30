
 
a = float(input("Enter first value: "))
b= float(input("Enter second value: "))
i= int(input("for plus write 1 \nfor minus write 2 \nfor multiply write 3 \nfor devision write 4 \nfor power write 5\nfor reminder write 6 \nEnter: "))


if i==1:
    c=a+b
elif i==2:
    c=a-b
elif i==3:
    c=a*b
elif i==4:
    c=a/b
elif i==5:
    c=a**b
elif i==6:
  c=a%b
else:
    print("Wrong input")
    c=None
    
 
if c is not None:
 print(c)
