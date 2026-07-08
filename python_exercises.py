#clock countdown timer code
import time
x=int(input("enter time in seconds"))
seconds=x/60
minutes=(seconds%60)/60
for a in range(x,0,-1):
    time.sleep(1)
    print(f"the time is 00:{minutes:02}:{a:02}")