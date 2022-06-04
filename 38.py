num=int(input("enter the num you want to find the avg"))
sum=0
for i in range(0,num+1,1):
    sum=sum+i
avg=sum/num
print("Sum of number is ",sum)
print("The avg of sum",avg)
