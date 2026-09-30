# with open("testing.txt","x") as f:
#     f.write("Im learning Java. \nJava is my fevourite language")
#     f.write("\nDo you want to learn java?") 



# with open("testing.txt","r") as f:
#     data=f.read()
#     new=data.replace("Java","python")
#     print(new)#it just change here not file. 

# with open("testing.txt","w") as f:
#     f.write(new)#here change the file


word='learnn'
with open("testing.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
        print("Found")
    else: print("Not Found")
