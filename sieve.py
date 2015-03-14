import numpy

# XXX: We probably ought to provide a shorter name.
# TODO: Figure out how this works and comment it.
def eratosthenes(n):
    '''
    Find all primes below a given value n > 6 using the Sieve of Eratosthenes.

    Code adapted from Robert William Hanks' primesfrom2to method found at:
        http://stackoverflow.com/a/3035188
    '''

    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype = numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False

    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

