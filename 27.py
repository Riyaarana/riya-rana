maths=float(input("enter maths marks:"))
chem=float(input("enter chemistry marks:"))
bio=float(input("enter bio marks:"))
eng=float(input("enter english marks:"))
hin=float(input("enter hindi marks:"))
per=(maths+chem+bio+eng+hin)*100/500
if(per>60):
    print("A grade")
elif(per<60)and(per>50):
    print("B grade")
else:
    print("C grade")
