import unittest
from Lab4Tests.Rational import *

a = Rational(1,1)
b = Rational(10,20)
c = Rational(-5,-7)
d = Rational(3,-3)
e = Rational(-7,7)
f = Rational(0,1)
g = Rational(1, 99999999999999999999999999999999999)
h = Rational(1, 0.00000000000000000000000000000001)


class TestMul(unittest.TestCase):

    def test_multiplyByOne(self):
        self.assertTrue(a.__mul__(a) == Rational(1, 1))
        self.assertTrue(a.__mul__(b) == Rational(10,20))
        self.assertTrue(a.__mul__(c) == Rational(-5, -7))
        self.assertTrue(a.__mul__(d) == Rational(3, -3))
        self.assertTrue(a.__mul__(e) == Rational(-7, 7))
        self.assertTrue(a.__mul__(f) == Rational(0, 1))
        self.assertTrue(a.__mul__(g) == Rational(1, 99999999999999999999999999999999999))
        self.assertTrue(a.__mul__(h) == Rational(1, 0.00000000000000000000000000000001))

    def test_multiplyByZero(self):
        self.assertTrue(f.__mul__(a) == Rational(0, 1))
        self.assertTrue(f.__mul__(b) == Rational(0, 20))
        self.assertTrue(f.__mul__(c) == Rational(0, -7))
        self.assertTrue(f.__mul__(d) == Rational(0, -3))
        self.assertTrue(f.__mul__(e) == Rational(0, 7))
        self.assertTrue(f.__mul__(f) == Rational(0, 1))
        self.assertTrue(f.__mul__(g) == Rational(0, 99999999999999999999999999999999999))
        self.assertTrue(f.__mul__(h) == Rational(0, 0.00000000000000000000000000000001))

    def test_multiplyBySelf(self):
        self.assertTrue(a.__mul__(a) == Rational(1, 1))
        self.assertTrue(b.__mul__(b) == Rational(100, 400))
        self.assertTrue(c.__mul__(c) == Rational(25, 49))
        self.assertTrue(d.__mul__(d) == Rational(9, 9))
        self.assertTrue(e.__mul__(e) == Rational(49, 49))
        self.assertTrue(f.__mul__(f) == Rational(0, 1))
        self.assertTrue(
            g.__mul__(g) == Rational(1, 9999999999999999999999999999999999800000000000000000000000000000000001))

    def test_multiplyByNegativeDenominator(self):
        self.assertTrue(d.__mul__(a) == Rational(3, -3))
        self.assertTrue(d.__mul__(b) == Rational(30, -60))
        self.assertTrue(d.__mul__(c) == Rational(-15, 21))
        self.assertTrue(d.__mul__(d) == Rational(9, 9))
        self.assertTrue(d.__mul__(e) == Rational(-21, -21))
        self.assertTrue(d.__mul__(f) == Rational(0, -3))
        self.assertTrue(d.__mul__(g) == Rational(3, -299999999999999999999999999999999997))

    def test_multiplyByNegativeNumerator(self):
        self.assertTrue(e.__mul__(a) == Rational(-7, 7))
        self.assertTrue(e.__mul__(b) == Rational(-70, 140))
        self.assertTrue(e.__mul__(c) == Rational(35, -49))
        self.assertTrue(e.__mul__(d) == Rational(-21, -21))
        self.assertTrue(e.__mul__(e) == Rational(49, 49))
        self.assertTrue(e.__mul__(f) == Rational(0, 7))
        self.assertTrue(e.__mul__(g) == Rational(-7, 699999999999999999999999999999999993))

    def test_multiplyByNegativeRational(self):
        self.assertTrue(c.__mul__(a) == Rational(-5, -7))
        self.assertTrue(c.__mul__(b) == Rational(-50, -140))
        self.assertTrue(c.__mul__(c) == Rational(25, 49))
        self.assertTrue(c.__mul__(d) == Rational(-15, 21))
        self.assertTrue(c.__mul__(e) == Rational(35, -49))
        self.assertTrue(c.__mul__(f) == Rational(0, -7))
        self.assertTrue(c.__mul__(g) == Rational(-5, -699999999999999999999999999999999993))

        def test_init_zero_denominator(self):
            num = 3
            den = 0

            Rational(num, den)

            self.assertRaises(ZeroDivisionError)


if __name__ == '__main__':
    unittest.main()
