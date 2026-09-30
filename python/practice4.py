#even odd detector
def waf(a):
    if(a%2==0):
        print(a ,"is even")
    else:
        print(a ,"is odd")
#vowel counter
def waf2(stringgg):
    stringg =stringgg.lower()
    c=0
    for i in stringg:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            c += 1
    print(c)
#Prime number detector
def waf3(a):
    c=0
    for i in range(1,a,1):
        if(a%i==0):
            c+=1
    if(c>2):
        print(a, "is not prime")
    else:
        print(a, "is prime")
#Avereg of the list
def waf4(listt):
    c=0
    for i in listt:
        c = c+i
    cc = len(listt)
    ccc=c/cc
    print(ccc)


waf4([2,3,1,4])
waf3(73)
waf2("fuck yoU")
waf(87)