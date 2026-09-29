#factorial
n=int(input("enter the number for factorial"))
fact=1
for a in range(1,n+1):
    fact=fact*a
print(f"the factorial  of {n} is {fact}")