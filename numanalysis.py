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
    x = 0.0
    for i in range(n):
        if i % 2 == 1:
            x = x - (1 / (3**i * (1 + 2 * i)))
        elif i % 2 == 0:
            x = x + (1 / (3**i * (1 + 2 * i)))
    return sqrt(12) * x


print(approxPi(31))
