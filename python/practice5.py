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
#Check any word exist which line
def line_check(word):
    data = True
    line_no=1
    with open("testing.txt","r") as f:
      while data:
          data = f.readline()
          if(word in data):  
              return line_no
          line_no += 1
    
    return "not found this word"    

print(line_check("wantt") )

#find even number from number file

def even_number_finder():
    count=0
    with open("number.txt","r") as f:
        data = f.read()
        num=data.split(",")
        for i in num:
            if(int(i)%2==0):
                count+=1
    print(count)

even_number_finder()


def odd_number_finder():
    count=0
    with open("number.txt","r") as f:
        data = f.read()
        num=data.split(",")
        i=0
        while i< len(num):
            if(int(num[i])%2 != 0):
                count+=1
            i+=1
    print(count)

odd_number_finder()
