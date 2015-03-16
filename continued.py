from frac import Fraction

def toFrac(terms):
    '''
    Turn the terms of a continued fraction into a regular fraction.
    '''

    # This is horrifying, but it lets us avoid special-casing the last term.
    ans = Fraction(1, 0)

    # Evaluate the continued fraction from the bottom up.
    for x in terms[::-1]:
        ans = ans.reciprocal() + x

    return ans

def getTerms(x, max_terms):
    '''
    Find the terms in the continued fraction for a number.
    '''
    # TODO: Handle negative x.

    # If x is 0, we're done.
    if not x:
        return [0]

    # Avoid special-casing the first term.
    x = 1 / x

    # Build the continued fraction from the top down.
    ans = []
    while x and max_terms > 0:
        max_terms -= 1
        x = 1 / x
        term = int(x)
        ans += [term]
        x -= term

    return ans

