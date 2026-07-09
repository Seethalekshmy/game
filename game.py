#to implement number guessing game
import random
x = random.randint(1, 6)
n=0
print("number in range 1 to 6")
while n<3 :
    a = int(input("enter your guess: "))
    n+=1
    if (a==x):
        print("Eureka!!!Guessed Right")
        break
    elif (n<3):
        print("Try again")
print("chances exceed!!the value is",x)
