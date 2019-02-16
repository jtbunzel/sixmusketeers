class Rational:
    """
    An instance represents a rational number.
    Numerator and denominator reduced to lowest terms.
    Denominator must be positive.
    """

    def __init__(self, a=0, b=1):
        """Constructor for Rational.
        """
        if b == 0:
            raise (ZeroDivisionError("Denom may not be zero."))
        else:
            self.n = a
            self.d = b

    def __add__(self, other):
        """Add two rational numbers.
        """
        return Rational()

    def __sub__(self, other):
        """Return self minus other.
        """
        return Rational()

    def __mul__(self, other):
        """Implement multiplication.
        """
        return Rational()

    def __div__(self, other):
        """Implement division.
        """
        return Rational()

    def __str__(self):
        """Display self as a string.
        """
        return "0/1"

    def __float__(self):
        """Implement the float() conversion function.
        """
        result = float((self.n / self.d))
        return result

    def __eq__(self, other, msg = None):
        return self.n == other.n and self.d == other.d
