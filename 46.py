maximum = int(input(" Please Enter the Maximum Value : "))
Eventotal = 0
 
for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        Eventotal = Eventotal + number
 
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Eventotal)) 
