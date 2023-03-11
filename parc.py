#Absolute Beginner

# Answer 4

# a= float(input('temperature value in Celsius\n'))
# b=(a*9/5)+32
# print(b)

#AB Q3

# a = float(input("Please enter the length "))
# b = float(input("Please enter the breadth "))
# area_rectangle = round(a*b,1)
# print("Area of rectangle is ",area_rectangle)


# a = list(range(10))
# b = list(range(10))
# c = list(range(10))

# def square(k):
#     return(k*k)

# a_square = []
# b_square = []
# c_square = []

# for i in a:
#     a_square.append(square(i))

# for i in b:
#     b_square.append(square(i))
    
# for i in c:
#     c_square.append(square(i))

# a_square_dict = dict (zip(a,a_square))
# b_square_dict = dict (zip(b,b_square))
# c_square_dict = dict (zip(c,c_square))

# sum_of_squares = 0
# for a_key,a_value in a_square_dict.items():
#     if a_key>0:
#         for b_key,b_value in b_square_dict.items():
#             if b_key>0:
#                 sum_of_squares = a_value + b_value
#             for c_key,c_value in c_square_dict.items():
#                 if c_key>0:
#                     if sum_of_squares ==  c_value:
#                         print("The pythagoras_triplet are", a_key, b_key, c_key)

# a=list(range(1,100))
# for i in a:
#     if a%2==0:
#         print(a,end=" ")

#PRIME NUMBER CODE
a = int(input("Start point\n"))
b = int(input("End point\n"))
for number in range(a,b):
    for i in range(2,number):
        if number%i==0:
             break
    else:
     print(number)

# number_list = list(range(2,101))
# print(number_list)

# for i in number_list:
#     if i%2==0:
#         number_list.remove(i)
# print(number_list)