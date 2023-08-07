date=int(input("Enter Date: "))
month=int(input("Enter Month: "))
year=int(input("Enter year: "))
quos=int((int(year/100))*100)
rem=year%100
ly= int(rem/4)
nly=rem-ly

if month==1:
    month=0
if month==2:
    month=3
if month==3:
    month=3
if month==4:
    month=6
if month==5:
    month=1
if month==6:
    month=4
if month==7:
    month=6
if month==8:
    month=2
if month==9:
    month=5
if month==10:
    month=0
if month==11:
    month=3
if month==12:
    month=5

if quos==1200 or quos==1600  or quos==2000:
    quos=6
if quos==1300 or quos==1700  or quos==2200:
    quos=4
if quos==1400 or quos==1800  or quos==2400:
    quos=2
if quos==1500 or quos==1900  or quos==2600:
    quos=0

cal = int(date+month+quos+(ly*2)+nly)
cal=cal%7
if cal==0:
    print("Day: Sunday")
if cal==1:
    print("Day: Monday")
if cal==2:
    print("Day: Tuesday")
if cal==3:
    print("Day: Wednesday")
if cal==4:
    print("Day: Thusday")
if cal==5:
    print("Day: Friday")
if cal==6:
    print("Day: Saturday")

