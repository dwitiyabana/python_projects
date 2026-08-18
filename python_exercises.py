#concession program
menu = {"popcorn small":500,
         "popcorn big":650,
         "popcorn jumbo":750,
         "diet coke":100,
         "ice cream":120}
cart=[]
for key, value in menu.items():
    print(f"the menu is {key}:{value}")
while True:
    food=input("enter the food you wanna eat (q to quit)").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("this item is not available")
total=0
for food in cart:
    total +=menu[food]
print("the items are")
for food in cart:
    print(f"{food}:{menu[food]}")

print(f"the total rupees is {total}")   