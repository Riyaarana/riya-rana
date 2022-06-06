n1=int(input("enter first num:"))
order=len(str(n1))
sum=0
temp=n1
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if n1==sum:
    print("it is an armstrong num")
else:
    print("it is not an armstrong num")
