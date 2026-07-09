#right angle triangle printing
length=int(input("enter the length"))
for x in range(length):
    for y in range(x):
        print("@", end=" ")
    print()