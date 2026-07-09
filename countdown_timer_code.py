#basic clock countdown timer code
import time
x=int(input("enter time in seconds"))
for a in range(x,0,-1):
    seconds=a%60
    minutes=int(a/60)%60
    hrs=int(a/3600)
    print(f"the time is {hrs:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("THE TIMES OVER!!!")