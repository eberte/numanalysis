import math


def e(n):
    '''
    Function 4.5.3
    '''
    sum = 0
    for i in range(n):
        sum = sum + 1/math.factorial(i)
    return sum


'''
4.5.4
Everytime the factorial function is called, it's doing the factorial of a
larger and larger number. The result is that every single time a factorial is
called, it performs the previous factorial and then a little more
'''


def eff_e(n):
    '''
    Function 4.5.5
    '''
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
    return sum


def leibniz():
    '''
    4.5.6
    '''
    sum = 0
    i = 0
    while abs((-1) ** i / (2 * i + 1)) > 0.000001:
        sum = sum + (-1) ** i / (2 * i + 1)
        i += 1
    pi = sum * 4
    return pi


def leib(x):
    sum = 0
    for i in range(x):
        sum = sum + (-1) ** i / (2 * i + 1)
    pi = 4 * sum
    return pi


def wallis(terms):
    product = 0
    if terms % 2 == 0:
        for i in range(int(terms / 2)):
            listTerms = []
            listTerms.append((2 * (i + 1)) / (2 * i + 1))
            listTerms.append((2 * (i + 1)) / (2 * i + 3))
    else:
        for i in range(int(terms / 2) + 1):
            listTerms = []
            listTerms.append((2 * (i + 1)) / (2 * i + 1))
            listTerms.append((2 * (i + 1)) / (2 * i + 3))
            del listTerms[2(terms / 2 + 1)]
    return listTerms


print(wallis(10))
