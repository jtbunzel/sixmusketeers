import unittest
from Rational import *

a = Rational(1,1)
b = Rational(10,20)
c = Rational(-5,-7)
d = Rational(3,-3)
e = Rational(-7,7)
f = Rational(0,1)


class TestMul(unittest.TestCase):

    def test_multiplyByOne(self):
        self.assertTrue(a.__mul__(a) == Rational(1, 1))
        self.assertTrue(a.__mul__(b) == Rational(10,20))
        self.assertTrue(a.__mul__(c) == Rational(-5, -7))
        self.assertTrue(a.__mul__(d) == Rational(3, -3))
        self.assertTrue(a.__mul__(e) == Rational(-7, 7))
        self.assertTrue(a.__mul__(f) == Rational(0, 1))

    def test_multiplyByZero(self):
        self.assertTrue(f.__mul__(a) == Rational(0, 1))
        self.assertTrue(f.__mul__(b) == Rational(0, 20))
        self.assertTrue(f.__mul__(c) == Rational(0, -7))
        self.assertTrue(f.__mul__(d) == Rational(0, -3))
        self.assertTrue(f.__mul__(e) == Rational(0, 7))
        self.assertTrue(f.__mul__(f) == Rational(0, 1))

    def test_multiplyBySelf(self):
        self.assertTrue(a.__mul__(a) == Rational(1, 1))
        self.assertTrue(b.__mul__(b) == Rational(100, 400))
        self.assertTrue(c.__mul__(c) == Rational(25, 49))
        self.assertTrue(d.__mul__(d) == Rational(9, 9))
        self.assertTrue(e.__mul__(e) == Rational(49, 49))
        self.assertTrue(f.__mul__(f) == Rational(0, 1))

    def test_multiplyByNegativeDenominator(self):
        self.assertTrue(d.__mul__(a) == Rational(3, -3))
        self.assertTrue(d.__mul__(b) == Rational(30, -60))
        self.assertTrue(d.__mul__(c) == Rational(-15, 21))
        self.assertTrue(d.__mul__(d) == Rational(9, 9))
        self.assertTrue(d.__mul__(e) == Rational(-21, -21))
        self.assertTrue(d.__mul__(f) == Rational(0, -3))

    def test_multiplyByNegativeNumerator(self):
        self.assertTrue(e.__mul__(a) == Rational(-7, 7))
        self.assertTrue(e.__mul__(b) == Rational(-70, 140))
        self.assertTrue(e.__mul__(c) == Rational(35, -49))
        self.assertTrue(e.__mul__(d) == Rational(-21, -21))
        self.assertTrue(e.__mul__(e) == Rational(49, 49))
        self.assertTrue(e.__mul__(f) == Rational(0, 7))

    def test_multiplyByNegativeRational(self):
        self.assertTrue(c.__mul__(a) == Rational(-5, -7))
        self.assertTrue(c.__mul__(b) == Rational(-50, -140))
        self.assertTrue(c.__mul__(c) == Rational(25, 49))
        self.assertTrue(c.__mul__(d) == Rational(-15, 21))
        self.assertTrue(c.__mul__(e) == Rational(35, -49))
        self.assertTrue(c.__mul__(f) == Rational(0, -7))


if __name__ == '__main__':
    unittest.main()
