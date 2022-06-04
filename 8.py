x=int(input("enter first num:"))
y=int(input("enter second num:"))
if(x>y):
    print("{0} is greater than {1}".format(x,y))
elif(y>x):
    print("{0} is greater than {1}".format(y,x))
else:
    print("both are equal")
