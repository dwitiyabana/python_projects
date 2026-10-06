#random number guessing 
import random

lowest_value = 1
highest_value = 10
origi_num = random.randint(lowest_value, highest_value)
guesses=0
running = True
while running:
    a=input(f"enter your guess in between {lowest_value} and {highest_value} ")
    if a.isdigit():
        a=int(a)
        guesses+=1
        if a>highest_value or a<lowest_value:
            print(f"enter your guess in between {lowest_value} and  {highest_value} ")
        elif a>origi_num:
            print("larger than answer")
        elif a<origi_num:
            print("smaller than answer")
        else:
            print(f"correct the answer was {origi_num}")
            print(f"guesses used are {guesses}")
            running = False
    else:
        print("wrong input")
        print(f"enter your guess in between {lowest_value} and {highest_value} ")