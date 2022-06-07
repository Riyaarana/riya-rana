n=int(input("enter the num:"))
flag=0
for i in range(1,n+1):
    if(i*(i+1)==n):
        flag=1
        break
if flag==1:
    print("its a pronic number")
else:
    print("not a pronic number")
