#Prime Number Checker
num=int(input("enter the number to check if its prime or not"))
if num==0 or num ==1:
    print(f"the number is {num}")
elif (num/2 or num/3 or num/5 or num/7)==0:
    print("no number is not prime")
else:
    print("the number is prime number")