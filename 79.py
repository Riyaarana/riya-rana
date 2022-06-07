n=int(input("enter the num:"))
rem=sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n//=10
print("the sum of digits",sum)
