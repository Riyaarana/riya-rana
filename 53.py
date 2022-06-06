n=int(input("enter the num:"))
if(n<0):
    print("enter the positive num")
elif (n==0):
    print(1)
else:
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    print("the factorial of",n,"is",fact)
