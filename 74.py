n=int(input("enter the num:"))
rem=0
sum=0
prod=1
while(n>0):
    rem=n%10
    sum=sum+rem
    prod=prod*rem
    n//=10
if(sum==prod):
    print("its a spy num")
else:
    print("its not a spy num")
