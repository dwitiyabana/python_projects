# rock paper scissors game

import random

options = ("rock", "paper", "scissors")

score = 0
match = True

while match:

    answer = random.choice(options)

    a = input("Enter your choice (rock, paper or scissors) or type 'end' to exit: ")
    a = a.lower()

    if a == "end":
        match = False

    elif a == answer:
        print(f"Computer chose {answer}")
        print("Tie")

    elif answer == "paper" and a == "rock":
        print(f"Computer chose {answer}")
        print("Computer won")

    elif answer == "rock" and a == "scissors":
        print(f"Computer chose {answer}")
        print("Computer won")

    elif answer == "scissors" and a == "rock":
        print(f"Computer chose {answer}")
        print("You won")
        score += 1

    elif answer == "paper" and a == "scissors":
        print(f"Computer chose {answer}")
        print("You won")
        score += 1

    elif answer == "rock" and a == "paper":
        print(f"Computer chose {answer}")
        print("You won")
        score += 1

    else:
        print(f"Computer chose {answer}")
        print("Computer won")

print(f"Score is {score}")