
sum=0
for i in range(1,11):
    num=int(input("number %d=" %i ))
    if(num>0):
        continue
    sum=sum+num
    print("sum of 10 by skipping negative num ",sum)
