def harshad(n):
    rem=sum=0
    while(n>0):
        rem=n%10
        sum=sum+rem
        n//=10
    return sum
for i in range (1,101):
   
    sum=harshad(i)
    if(i%sum==0):
        print(i,end=" ")
