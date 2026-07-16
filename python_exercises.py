#python quiz game
questions = ("How many elements are in the periodic table?: ",
              "Which animal lays the largest eggs?: ",
              "What is the most abundant gas in Earth's atmosphere?: ",
              "How many bones are in the human body?: ",
              "Which planet in the solar system is the hottest?: ")

options =   (("Α. 116", "B. 117", "C. 118", "D. 119"),
             ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
             ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
             ("Α. 206", "B. 207", "C. 208", "D. 209"),
             ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("c","d","a","a","b")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter the answer (A, B, C, D)").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("correct")
    else:
        print("incorrect")
        print(f"the correct answer is {answers[question_num].upper()}")
    question_num += 1
    print()
