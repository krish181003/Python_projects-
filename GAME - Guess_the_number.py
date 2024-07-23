import random

target = random.randint(1, 100)

def my_game(b):
    print("guess the correct number or to exit press 'x'")

    while True:

        b = input("num :")
        if (b == "x"):
            print("you quit")
            break 

        elif (int(b) == int(target)):
            print("you won! Hurrah")
            break 

        elif (int(b) < int(target)):
            print("think big")

        else:
            print("think small")

    print("_____Game Over_____")
    
my_game(target)
