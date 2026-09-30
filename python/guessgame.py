import random
a= (random.randint(1,50))

def wep (b):
  
  while True:
    c = int(input("Guess the lucky number: "))
    if c>b+5:
       print("Your number is too high, guess again")
    elif (c>b) and (c<=b+5):
        print("you are close, guess lower number ")
    elif c==b:
        print("congratulations!")
        break
    elif c<b-5:
        print("Your number is too low, guess again")
    elif (c<b) and (c>=b-5):
       print("You are close guess some upper")
        

wep(a)

