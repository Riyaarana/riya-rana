char=input("enter the character:")
if((char>='a'and char<='z')or(char>='A'and char<='Z')):
    print("its an alphabet")
elif(char>='0'and char<='9'):
    print("its a digit")
else:
    print("not a alphabet nor a digit")
