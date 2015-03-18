from common import gcd
from functools import total_ordering

@total_ordering
class Fraction:
    '''
    A class to handle operations on rational numbers.

    NOTE: This class does no sanity or type checking.
    You CAN divide by zero, if that's what you're into.
    '''

    #################
    ## Constructor ##
    #################

    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    #####################
    ## Type Conversion ##
    #####################

    def __str__(self):
        return str(self.numerator) + " / " + str(self.denominator)

    def __int__(self):
        # NOTE: This returns the floor, which is inconsistent with floats.
        return self.numerator // self.denominator

    def __float__(self):
        return float(self.numerator) / self.denominator

    def __bool__(self):
        return self.numerator != 0

    def __nonzero__(self):
        # Needed for Python 2
        return self.__bool__()

    ##########################
    ## Arithmetic operators ##
    ##########################

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __add__(self, other):
        newNumerator = self.numerator * other.denominator + \
                        self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Fraction(newNumerator, newDenominator)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    # FIXME: This doesn't allow division by integers.
    def __div__(self, other):
        return self * other.reciprocal()

    def __rdiv__(self, other):
        return other * self.reciprocal()

    def __mul__(self, other):
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Fraction(newNumerator, newDenominator)

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        newNumerator = self.numerator ** power
        newDenominator = self.denominator ** power
        return Fraction(newNumerator, newDenominator)

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def reduce(self):
        g = gcd(self.numerator, self.denominator)
        if g != 0:
            self.numerator /= g
            self.denominator /= g
        return self

    ##########################
    ## Comparison Operators ##
    ##########################

    def __eq__(self, other):
        return  self.numerator * other.denominator == \
                self.denominator * other.numerator

    def __lt__(self, other):
        return  self.numerator * other.denominator < \
                self.denominator * other.numerator

