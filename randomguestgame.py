import random
import os

number = random.randint(1,10)

print("Let's play a silly game! Guess the number between 1 and 10")
guess = input("Enter your number: ")
guess = int(guess)

if(guess== number):
    print("You Win!")
    
else:
    print("You lose!")