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
    pass


print(eff_e(5))
print(e(4))
