# Math Quiz

questions = (
    "5 + 7 = ?",
    "12 × 3 = ?",
    "20 ÷ 4 = ?"
)

options = (
    ("A. 10", "B. 12", "C. 13", "D. 14"),
    ("A. 36", "B. 30", "C. 24", "D. 48"),
    ("A. 4", "B. 5", "C. 6", "D. 7")
)

answers = ("b", "a", "b")

guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)

    # Print the options for the current question
    for option in options[question_num]:
        print(option)

    # Take user input
    guess = input("Enter your answer (A, B, C, D): ").lower()
    guesses.append(guess)

    # Check the answer
    if guess == answers[question_num]:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")
        print(f"The correct answer is {answers[question_num].upper()}")

    question_num += 1
    print()

# Display results
print("---------- RESULT ----------")

print("Correct Answers: ", end="")
for answer in answers:
    print(answer.upper(), end=" ")
print()

print("Your Guesses:    ", end="")
for guess in guesses:
    print(guess.upper(), end=" ")
print()

percentage = int((score / len(questions)) * 100)

print(f"Your Score: {score}/{len(questions)}")
print(f"Percentage: {percentage}%")