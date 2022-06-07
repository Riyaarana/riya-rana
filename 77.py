n=int(input("enter the num:"))
rem=sum=0
fact=1
temp=n
while(temp>0):
    rem=temp%10
    for i in range (1,rem+1):
        fact=fact*i
        i=i+1
    print()
    sum=sum+fact
    temp//=10
if(sum==n):
    print("its a strong num")
else:
    print("its not a strong num")
