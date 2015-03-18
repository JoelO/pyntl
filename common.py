# TODO: Rename this file.

def gcd(*args):
    '''
    Find the greatest common divisor.
    '''

    # The GCD of anything and 0 is itself.
    ans = 0

    # Apply the Euclidean Algorithm with each argument and the running total.
    for x in args:
        while ans != 0:
            ans, x = x % ans, ans
        ans = x

    return ans

def lcm(*args):
    '''
    Find the least common multiple.
    '''

    # The LCM of anything and 1 is itself.
    ans = 1

    # Use the fact that GCD(a, b) * LCM(a, b) = a * b.
    for x in args:
        if x == 0:
            return 0
        else:
            ans = x * ans / gcd(x, ans)

    return ans

