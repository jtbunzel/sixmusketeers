import unittest
from Lab4Tests import Rational


class TestSub(unittest.TestCase):
    def test_subtractBySelf(self):
        a = Rational('2', '3')
        b = Rational('2', '3')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('0', '3'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('0', '3'))

    def test_substractionOfTwoDifferentRationalNumbers(self):
        a = Rational('2', '3')
        b = Rational('5', '4')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('-7', '12'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('7', '12'))

    def test_substractionOfTwoNegativeDifferentRationalNumbers(self):
        a = Rational('-2', '3')
        b = Rational('-5', '4')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('7', '12'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('-7', '12'))

    def test_substractionOfNegativeAndPositiveDifferentRationalNumbers(self):
        a = Rational('2', '3')
        b = Rational('-5', '4')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('23', '12'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('-23', '12'))

    def test_substractionOfIntegerRationalNumbers(self):
        a = Rational('2', '1')
        b = Rational('5', '1')
        result = a.__sub__(b)
        self.assertEqual(result, Rational(-3, 1))
        result = b.__sub__(a)
        self.assertEqual(result, Rational(3, 1))
    def test_subOfRationalNumberWithDifferentSignOfNumAndDino(self):
        a = Rational('-2', '-3')
        b = Rational('5', '4')
        c = Rational('3', '-2')
        d= Rational('-1,', '3')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('-7', '12'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('7', '12'))
        result = a.__sub__(c)
        self.assertEqual(result, Rational('13', '6'))
        result = c.__sub__(a)
        self.assertEqual(result, Rational('-13', '6'))
        result = a.__sub__(d)
        self.assertEqual(result, Rational('-3', '3'))
        result = d.__sub__(a)
        self.assertEqual(result, Rational('-7', '6'))
        result = b.__sub__(c)
        self.assertEqual(result, Rational('11', '4'))
        result = c.__sub__(b)
        self.assertEqual(result, Rational('-11', '4'))
        result = b.__sub__(d)
        self.assertEqual(result, Rational('19', '12'))
        result = d.__sub__(b)
        self.assertEqual(result, Rational('-19', '12'))
        result = c.__sub__(d)
        self.assertEqual(result, Rational('-7', '6'))
        result = d.__sub__(c)
        self.assertEqual(result, Rational('7', '6'))

    def test_substractionOfTwoNegativeDifferentIntegerRationalNumbers(self):
        a = Rational('-2', '1')
        b = Rational('-5', '1')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('3', '1'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('-3', '1'))

    def test_substractionOfNegativeAndPositiveDifferentIntegerRationalNumbers(self):
        a = Rational('2', '1')
        b = Rational('-5', '1')
        result = a.__sub__(b)
        self.assertEqual(result, Rational('7', '12'))
        result = b.__sub__(a)
        self.assertEqual(result, Rational('-7', '12'))


    def test_substractionByZero(self):
        a = Rational('4', '3')
        b = Rational('0', '5')
        c = Rational('2', '0')
        d = Rational('2', '1')
        e= Rational('0', '0')
        self.assertRaises(a.__sub__(b), Rational('4', '3'))
        self.assertRaises(b.__sub__(a), Rational('-4', '3'))
        self.assertRaises(a.__sub__(c), Rational('4', '3'))
        self.assertRaises(c.__sub__(a), Rational('-4', '3'))
        self.assertRaises(d.__sub__(b), Rational('2', '1'))
        self.assertRaises(b.__sub__(d), Rational('-2', '1'))
        self.assertRaises(d.__sub__(c), Rational('2', '1'))
        self.assertRaises(c.__sub__(d), Rational('-2', '1'))
        self.assertRaises(a.__sub__(e), Rational('4', '3'))
        self.assertRaises(e.__sub__(a), Rational('-4', '3'))

if __name__ == '__main__':
    unittest.main()
