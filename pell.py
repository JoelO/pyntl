from math import sqrt
from continued import toFrac

# TODO: Factor this out.
def gcd(a, b):
    '''
    Find the greatest common divisor using the Euclidean Algorithm.
    '''
    while a != 0:
        (a, b) = (b % a, a)
    return b

def pell(n):
    '''
    Generate solutions (x, y) to x^2 - n y^2 = 1 for non-square n.
    '''

    # We find the principal solution using continued fractions.

    # At each step, we have a number of the form (a sqrt(n) + b) / c.
    root = int(sqrt(n))
    a = 1
    b = 0
    c = 1

    terms = []
    while True:
        # Peel off the next term for the continued fraction.
        d = (a * root + b) / c
        terms += [d]

        # Subtract off the integer part.
        b -= c * d

        # Take the reciprocal of what's left.
        a, b, c = c * a, -c * b, a * a * n - b * b

        # Common factors get out of hand if we're not careful.
        g = gcd(gcd(a, b), c)
        a /= g
        b /= g
        c /= g

        f = toFrac(terms)
        x_princ, y_princ = f.numerator, f.denominator
        if x_princ * x_princ - n * y_princ * y_princ == 1:
            break

    # Subsequent solutions can be found iteratively.
    x, y = x_princ, y_princ
    while True:
        yield (x, y)
        x, y = x_princ * x + n * y_princ * y, x_princ * y + y_princ * x

