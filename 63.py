n=int(input("enter the num:")) #harshad num which is divisible by its sum of digits
rem=sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n//=10
if(n%sum==0):
    print("it is harshad number")
else:
    print("it is not harshad number")
