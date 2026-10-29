import random

secret_number = random.randint(0,10)
guess = int(input("your guess : "))
while guess!= secret_number:
    if guess < secret_number:
       print("Your Guess is too low, try again")
    else:
       print("Your guess is too high, try again")
    guess = int(input("your guess : "))
print("you guess is right")
