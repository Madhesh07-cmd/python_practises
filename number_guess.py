import random
while(True):
    number=random.randint(1,100)
    print(number)
    guess=int(input("Guess a number between 1 and 100: "))
    if guess==number:
        print("Congratulations!")
        break
    elif guess<number:
        print("Too low")    
        break
    elif guess>number:
        print("Too high") 
        break  
    else:
        print("invalid", number)