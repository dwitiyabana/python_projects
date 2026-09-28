#Take two numbers and an operator (+, -, *, /) as input. (basic calculator)
num1=int(input("enter the 1st number"))
num2=int(input("enter 2nd number"))
while True:
    inp=input('''
_______what fucntion you wanna perform_______
enter (a) for addition
enter (s) for subtraction
enter (d) for division
enter (m) for multiplication
enter (p) for power  
enter (end) to exit
''')
    if inp.lower() == 'a':
        result=num1+num2
        print(result)
    elif inp.lower() == 's':
        result=num1-num2
        print(result)
    elif inp.lower() == 'd':
            result=num1/num2
            print(result)
    elif inp.lower() == 'm':
            result=num1*num2
            print(result)
    elif inp.lower() == 'p':
            result=num1**num2
            print(result)
    elif inp.lower() == 'end':
          break
    else:
          print("enter the correct choice")
    