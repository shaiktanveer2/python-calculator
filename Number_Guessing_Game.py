#Easy Number_Guessing_game without using any Functions and loops

import random 

secret=random.randint(1,50)
attempt=5

while attempt>0:
    guess=int(input("Enter Guess:"))
    
    if guess==secret:
        print("You Win!")
        
    elif guess>secret:
        print("too high")
        
    else:
        print("too low")
    attempt=attempt-1
    print("Attempt left:",attempt) 
    
if attempt==0:
    print("Game over")
    print("The number was:",secret)