#python compund interest calculator
p=float(input("enter the principle amount : "))
while p<=0:
    p=float(input("the principle amount cant be zero or negative enter again"))
r=float(input("enter the rate of interestrate of interest : "))
while r<=0:
    r=float(input("the rate of interest be zero or negative enter again : "))
t=int(input("enter the years"))
while t<=0:
    t=int(input("the time cant be zero or less than zero enter again : "))
a=p*(1+(r/100))**t
print(f"the compund interest is {a:.2f}")