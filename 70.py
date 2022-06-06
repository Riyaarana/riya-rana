n=int(input("enter the num"))
if n>1:
    for i in range(2,n):
        if( n%i==0):
            print("its not prime num")
           
        else:
            print("its a prime num")
        break
else:
    print("it is not a prime num")
