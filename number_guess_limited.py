import random

number = random.randint(1,20)
attempt = 0

while attempt < 7:
    guess = int(input("my guess is: "))
    attempt  = attempt + 1
    if guess == number:
        print(f"you found in {attempt} attempts")
        break
    elif guess < number:
        print("too low")
    else :
         print("too high")
if guess != number:
    print("lost! it was" , number) 
        
                
