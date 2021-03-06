import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        gcd1 = math.gcd(numerator, denominator)

        if denominator < 0:
            self.numerator = -(int(numerator/gcd1))
            self.denominator = abs(int(denominator/gcd1))
        elif denominator == 0:
            self.numerator = 1
            self.denominator = 0
        else:
            self.numerator = int(numerator/gcd1)
            self.denominator = int(denominator/gcd1)


    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = ((self.numerator *  frac.denominator) + (self.denominator * frac.numerator))
        denominator =  (self.denominator * frac.denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, frac):
        """Return the sum of two fractions subtracting each other (self - frac).
        """
        numerator = ((self.numerator *  frac.denominator) - (self.denominator * frac.numerator))
        denominator =  (self.denominator * frac.denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, frac):
        """Return the multiplying result of 2 fractions
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        gcd = math.gcd(numerator, denominator)

        return Fraction(int(numerator/gcd), int(denominator/gcd))
    
    def __str__(self):
        """Return the string of the Fraction to the user.
        """
        if self.denominator == 1:
            str = self.numerator/self.denominator
            return f"{int(str)}"
        # elif self.denominator == 0 or self.numerator == 0:
        #     return str(0)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2)

        """
        equal = self.numerator == other.numerator and self.denominator == other.denominator

        if equal == False:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)
            other.numerator = abs(other.numerator)
            other.denominator = abs(other.denominator)

            if self.numerator < other.numerator:
                smallnum = self.numerator
            else:
                smallnum = other.numerator

            if self.denominator < other.denominator:
                smallnum2 = self.denominator
            else:
                smallnum2 = other.denominator

            num1 = f"{smallnum}/{smallnum2}"

            gcd1 = math.gcd(self.numerator, other.numerator)
            gcd2 = math.gcd(self.denominator, other.denominator)

            num2 = f"{gcd1}/{gcd2}"

            return num1 == num2

        else:
            return equal
            
    def __gt__(self, other):
        """Return the boolean result of either the 2 fractions 
        are greater than each other or not, if not return False.
        """
        self.numerator = abs(self.numerator)
        self.denominator = abs(self.denominator)
        other.numerator = abs(other.numerator)
        other.denominator = abs(other.denominator)

        num1 = (self.numerator/other.numerator)
        num2 = (self.denominator/other.denominator)

        if num1 > num2:
            return True
        else:
            return False