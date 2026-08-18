rows = int(input("enter the number of rows for the structure"))
columns = int(input("enter the number of colums for the structure "))
symbol = input("enter the symbols")
for x in range (0,rows):
    for y in range(0,columns+1):
        print(symbol, end="")
    print()
