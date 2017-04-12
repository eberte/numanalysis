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


def eff_e(n):
    sum = 0
    pass


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
    x = 1.0
    for i in range(terms):
        x = x * 2 / vieteHelp(i)

    return x
