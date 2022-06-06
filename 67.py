n=int(input("enter the num:"))
rem=0
reverse=0
temp=n
while(temp>0):
    rem=temp%10
    reverse=(reverse*10)+rem
    temp//=10
    
if(n==reverse):
    print("its a palindrom")
else:
    print("its not a palindrom")
