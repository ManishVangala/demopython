import math
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        fact1= n*fact(n-1)
        return fact1

print(fact(0))
print(fact(12))