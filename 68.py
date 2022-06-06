print("List of palindrome num ")

for i in range(1,101):
    temp=i
    reverse=0
    while(temp>0):
        rem=temp%10
        reverse=(reverse*10)+rem
        temp//=10
    if(i==reverse):
        print(i)
