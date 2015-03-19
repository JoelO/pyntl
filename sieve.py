import numpy

# XXX: We probably ought to provide a shorter name.
def eratosthenes(n):
    '''
    Find all primes below a given value n > 6 using the Sieve of Eratosthenes.

    Code adapted from Robert William Hanks' primesfrom2to method found at:
        http://stackoverflow.com/a/3035188
    '''

    # We only need to keep track of numbers that are 1 and 5 mod 6.
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype = numpy.bool)

    # Cross out multiples of each prime below sqrt(n).
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        # Check that the index corresponds to a prime.
        if sieve[i]:
            # Find the prime it corresponds to.
            k = 3 * i + 1 | 1

            # Find the index of each multiple and cross it out.
            sieve[k * k / 3 : : 2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3 : : 2 * k] = False

    # Make sure to remember 2 and 3 are prime.
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

