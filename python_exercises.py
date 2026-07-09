#right angle triangle printing
length=int(input("enter the length"))
for x in range(length, 0, -1):
    for y in range(x):
        print("@", end=" ")
    print()