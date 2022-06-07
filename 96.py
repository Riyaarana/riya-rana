str=input("enter the string:")
char=input("enter the char to find frquency:")
count=0
for i in range(len(str)):
    if(str[i]==char):
        count=count+1
print("the frequency of ",char,"in string is ",count)
