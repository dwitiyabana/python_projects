# String Analyzer

string1 = input("Enter a string: ")

vowels = ("a", "e", "i", "o", "u")

count_vowels = 0
count_consonants = 0
count_digits = 0
count_spaces = 0

for a in string1.lower():

    if a in vowels:
        count_vowels += 1

    elif a.isdigit():
        count_digits += 1

    elif a == " ":
        count_spaces += 1

    elif a.isalpha():
        count_consonants += 1

print("Total characters:", len(string1))
print("Vowels:", count_vowels)
print("Consonants:", count_consonants)
print("Digits:", count_digits)
print("Spaces:", count_spaces)