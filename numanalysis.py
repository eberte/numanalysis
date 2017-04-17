import math
# pg 166


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


def wallis(terms):
    product = 1
    listTerms = []
    if terms % 2 == 0:
        for i in range(int(terms / 2)):
            listTerms.append((2 * (i + 1)) / (2 * i + 1))
            listTerms.append((2 * (i + 1)) / (2 * i + 3))
    else:
        for i in range(int((terms + 1) / 2)):
            listTerms.append((2 * (i + 1)) / (2 * i + 1))
            listTerms.append((2 * (i + 1)) / (2 * i + 3))
            del listTerms[2(terms / 2 + 1)]
    return listTerms


def sqrt(n):
    """Approximates the square root of n until |x| is small enough.

    Parameters:
        n: number to take the square root of

    Return value:
        the approximate square root of n
    """
    x = 1.0
    k = 0
    while abs(x - k) > 10 ** -15:
        k = x
        x = 0.5 * (x + n / x)
    return x


def approxPi(n):
    """
    Approximates pi using Madhava Sangamagrama's method

    Parameters:
        n: number of terms to use

    Return value:
        the approximate value of pi

    useless to run past 30 iterations: floats are not long/accurate enough
    """
    x = 0.0
    for i in range(n):
        if i % 2 == 1:
            x = x - (1 / (3**i * (1 + 2 * i)))
        elif i % 2 == 0:
            x = x + (1 / (3**i * (1 + 2 * i)))
    return sqrt(12) * x


def nilakantha(terms):
    """
    Approximates pi using the nilakantha series with the number of terms
    input buy user

    Parameters:
        terms: number of terms to use

    Return value:
        the approximate value of pi

    *function breaks at 10^-15 and does not return the correct digit
    """
    x = 0.0
    for i in range(terms):
        if i % 2 == 1:
            x = x - (4 / ((i * 2 + 2) * (i * 2 + 3) * (i * 2 + 4)))
        elif i % 2 == 0:
            x = x + (4 / ((i * 2 + 2) * (i * 2 + 3) * (i * 2 + 4)))
    return 3 + x


def vieteHelp(terms):
    """
    Helps the viete function by producing the denominator
    """
    if terms == 1:
        return sqrt(2)
    elif terms == 0:
        return 1
    else:
        return sqrt(2 + vieteHelp(terms - 1))


def viete(terms):
    """
    Approximates pi using the viete series with the number of terms
    input buy user

    Parameters:
        terms: number of terms to use

    Return value:
        the approximate value of pi
    """
    x = 1.0
    for i in range(terms):
        x = x * 2 / vieteHelp(i)
    return x
