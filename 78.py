import math
for i in range (1,100):
    temp=i
    sum=0
    while(temp>0):
        rem=temp%10
        fact=math.factorial(rem)
        sum=sum+fact
        temp//=10
    if(sum==i):
        print(i)
