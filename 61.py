def sumofdigit(n):
    rem=0
    sum=0
    if(n>0):
        rem=n%10
        sum=sum+rem*rem
        n=n//10
    return sum
n=int(input("enter the number "))
result=n
while(result!=1 and result!=4):
    result=sumofdigit(result)
if(result==1):
    print("its a happy number")
else:
    print("it is not happy num")
