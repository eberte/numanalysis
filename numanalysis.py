import math


def e(n):
    '''
    Function 4.5.3
    '''
    sum = 0
    for i in range(n):
        sum = sum + 1/math.factorial(i)
    return sum


def eff_e(n):
    sum = 0
    denom = 1
    for i in range(n):
        sum = sum + 1/denom
        denom = denom * (denom + 1)
    return sum

print(e(5))
print(eff_e(5))
