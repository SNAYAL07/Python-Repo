'''price=int(input("Please give the price"))
if price<60:
    print("dont buy")
elif price>=60 and price<=80:
    range=int(input("Select range "))
    if range<100:
        print("choose another range")
    else:
        warranty=int(input("Enter warranty "))
        if warranty<3:
            print("dont buy")
        else:
            print("buy")
else:
    range1=int(input("Gib range"))
    if range1<100:
        warranty=int(input("Gib warranty "))
        if warranty>3:
            print("buy")
        else:
            print("dont buy")
    else:
        print("dont buy")'''

import Psutil
print(psutil.cpu_percent(5))