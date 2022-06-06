num=int(input("Enter the num:"))
count=0
while num!=0:
    num//=10
    count+=1

print(" total digits are "+str(count))
