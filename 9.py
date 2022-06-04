x=int(input("enter first num:"))
y=int(input("enter second num:"))
z=int(input("enter third num:"))
if(x>y)and(x>z):
    largest=x
elif(y>x)and(y>z):
    largest=y
else:
    largest=z
print("The largest num is ",largest)
