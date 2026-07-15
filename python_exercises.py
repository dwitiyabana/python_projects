#shopping cart program
food=[]
price=[]
total = 0
while True:
    foods=input("enter the food you wanna eat (q to quit) : ")
    if foods.lower() == "q" :
        break
    else:
        prices=float(input("enter the prices for the food : $"))
        food.append(foods)
        price.append(prices)
print("the shopping cart is ->")
for x in food:
    print(x)
for y in price:
    total+=y
print(f"the total is {total}")
