# Finding PRIME NUMBER within input range
a = int(input("Start point\n"))
b = int(input("End point\n"))
for number in range(a,b):
    for i in range(2,number):
        if number%i==0:
             break
    else:
     print(number)