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
    factorial = 1
    counter = 1
    for i in range(n):
        if factorial == 0:
            sum = 1
            counter += 1
        else:
            sum = sum + 1/factorial
            factorial = factorial * counter
            counter += 1
    return sum, factorial, counter

print(eff_e(5))
print(e(5))
