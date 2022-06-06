from datetime import datetime
now=datetime.now()
print("now = ",now)
string=now.strftime("%d/%m/%Y %H:%M")
print("date and time =",string)
