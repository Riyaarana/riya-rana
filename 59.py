n1=int(input("enter first num:"))
order=len(str(n1))
sum=0

temp=n1
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
    order=order-1
print("the sum of digit ",sum)
if n1==sum:
    print("it is disarium num")
else:
    print("it is not disarium num")
