#rock paper scissor game 
import random

options = ("rock", "paper", "scissors")
score=0
match = True
while match:
    answer = random.choice(options)
    a=input("enter your choice (rock or paper or scissor)")
    a=a.lower()
    if a==answer:
        print("tie")
    else:
        if answer == "paper" and a == "rock":
            print("computer won")
        elif answer == "rock" and a == "scissors":
            print("computer won")
        elif answer == "scissors" and a == "rock":
            print ("you won")  
            score+=1
            match=False
        elif answer == "paper" and a == "scissors":
            print ("you won")  
            score+=1
            match=False
        elif answer == "rock" and a == "paper":
            print ("you won")  
            score+=1
            match=False
        else:
            print("computer won")
print(f"score is {score}")