import random
a= (random.randint(1,50))

def game(b):
    c = int(input("Guess the lucky number: "))
    if(c==b):
        print("congratulations!")
        return
    if c>b+5:
        print("Your number is too high, guess again")
        game(b)
    if (c>b) and (c<=b+5):
        print("you are close, guess lower number ")
        game(b)
    if c<b-5:
            print("Your number is too low, guess again")
            game(b)
    if (c<b) and (c>=b-5):
           print("You are close guess some upper")
           game(b)

# game(a)
print(type(game))

def factor(n):
     if (n==0) or (n==1):
          return 1
     return n*factor(n-1)

print(factor(4))

def sum(m,o):
     if(m>o):
          return 0
     return m+sum(m+1,o)

print(sum(1,10))