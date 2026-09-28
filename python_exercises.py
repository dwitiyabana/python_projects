#Take an integer as input and print: Whether it's positive, negative, or zero / Whether it's even or odd
inp=int(input("enter the number to check Whether it's positive, negative, or zero / Whether it's even or odd "))
if inp == 0:
    print("the number is zero")
elif inp >= 0:
    print("the number is positive")
else:
    print("the number is negative")

if inp==0:
    print()
elif inp%2==0:
    print("the number is even")
else:
    print("the number is odd")

    