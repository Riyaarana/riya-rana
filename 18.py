cp=int(input("enter the cost price:"))
sp=int (input("enter the selling price:"))
if(cp>sp):
    amount=cp-sp
    print("Total loss amount is {0}".format(amount))
elif(sp>cp):
    amount=sp-cp
    print("Total profit amount is {0}".format(amount))
else:
    print("There is No Profit No Loss!")
