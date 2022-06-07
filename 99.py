str=input("enter the string:")
count=0
for i in range(0,len(str)):
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' 
    or str[i]=='A' or str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):
            count=count+1
print("total number of vowels in string:",count)
