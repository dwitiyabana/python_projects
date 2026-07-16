#basic dialer display matrix program
a=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for collection in a:
    for elements in collection:
        print(elements, end = " ")
    print()