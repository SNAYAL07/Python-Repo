#n! = 1*2*3*4*.....n
#n! = [1*2*2*3...n-1]*n
#n! = (n-1)!*n

# n = 4
# product = 1

# for i in range(n):
#     product=product*(i+1)

# print(product)

def factorial_recursive(n):
    if n==1 or n==0:      #use to stop the func from infinitely callin itself
        return 1
    return n*factorial_recursive(n-1)

f = factorial_recursive(7)
print(f)