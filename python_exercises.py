username=input("enter the username (must be under 12 characters, no spaces, no digits)")
if not username.find(" ")==-1:
    print("the username cant have spaces")
elif username.isalpha and len(username)<=12:
    print("the username is correct")
else:
    print("wrong")