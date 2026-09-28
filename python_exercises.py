#take n as input and calculate sum and avg using loop and logic
n=int(input("enter the integer to calculate sum and its avg"))   
sum=0
for a in range(0,n+1):
    sum+=a
print(f"the sum is {sum}")
avg=sum/n
print(f"the average is {avg}")