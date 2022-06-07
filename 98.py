str=input("enter the string:")
count=1
for i in range(len(str)):
    if(str[i]==" " or str=='\n' or str=='\t'):
        count=count+1
print("the total words in string:",count)
