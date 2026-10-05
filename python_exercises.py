#Prime Number Checker
num = int(input("Enter the number: "))
if num < 2:
    print("Neither prime nor composite")
else:
    is_prime = True
    for a in range(2, num):
        if num % a == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")