import cmath

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
d=(b**2)-(4*a*c) #discriminant
s1=(-b-cmath.sqrt(d))/(2*a)
s2=(-b+cmath.sqrt(d))/(2*a)
print("roots are {0} and {1}".format(s1,s2))
