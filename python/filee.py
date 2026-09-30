# f=open("shakib.txt","r")
# data = f.read()
# print(data)
# f.close()

# f=open("shakib.txt","a")
# f.write("Tamim ia a gay")#add to the last


# f=open("shakib.txt","r")
# data = f.read()
# print(data)

f=open("shakib.txt","r+")#use for read and write
print(f.read())
f.write("\nWho is tamim?")
