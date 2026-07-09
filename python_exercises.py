#rectangle printing
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
for x in range (breadth):
    for y in range (length):
        print("*", end=" ")
    print()
    
