n=int(input("enter the num:"))
sq=n*n
sum=0
rem=0
while(sq>0):
    rem=sq%10
    sum=sum+rem
    sq//=10
if(n==sum):
    print("neon num")
else:
    print("not a neon num")
