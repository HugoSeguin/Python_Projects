#Guessing Game
import random

x = int(random.randint(1,100))

truth = False
while(truth == False):
    print("Guess the number")
    guess = int(input())
    if(guess < x):
        print("too low")
    if (guess > x):
        print("too high")
    if (guess == x):
        print("Correct!")
        truth = True
print(x)

