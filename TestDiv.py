import unittest
from Rational import *

class TestDiv(unittest.TestCase):
    
    def test_DivisionBySelf(self):
        a = Rational(7, 2)
        b = Rational(7, 2)
        result = a.__div__(b)
        self.assertEqual(result, Rational(1, 1))

    def test_DivisionOfTwoDifferentRationalNumbers(self):
        a = Rational(2, 3)
        b = Rational(5, 8)
        result = a.__div__(b)
        self.assertEqual(result, Rational(16, 15))

    def test_DivisionOfTwoIntegers(self):
        a = Rational(3, 1)
        b = Rational(5, 1)
        result = a.__div__(b)
        self.assertEqual(result, Rational(3, 5))

    def test_DivisionByZero(self):
        a = Rational(4, 3)
        b = Rational(0, 1)
        self.assertRaises(a.__div__(b), ZeroDivisionError)

    def test_ReductionOfAnswer(self):
        a = Rational(2, 3)
        b = Rational(3, 4)
        result = a.__div__(b)
        self.assertEqual(result, Rational(1, 2))

if __name__ == '__main__':
    unittest.main()
