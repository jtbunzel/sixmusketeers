import unittest
from Lab4Tests import Rational


class TestAdd(unittest.TestCase):
    def test_AddBySelf(self):
        a = Rational('5', '3')
        b = Rational('5', '3')
        c = Rational('-4', '2')
        d = Rational('-4', '2')
        e = Rational('-7', '-4')
        f = Rational('-7', '-4')
        g = Rational('8', '-9')
        h = Rational('8', '-9')
        result1 = a.__add__(b)
        result2 = c.__add__(d)
        result3 = e.__add__(f)
        result4 = g.__add__(h)
        self.assertEqual(result1, Rational('10', '3'))
        self.assertEqual(result2, Rational('-4', '1'))
        self.assertEqual(result3, Rational('-7', '2'))
        self.assertEqual(result4, Rational('-16', '9'))

    def test_AdditionOfTwoDifferentRationalNumbers(self):
        a = Rational('5', '3')
        b = Rational('5', '2')
        c = Rational('-4', '3')
        d = Rational('-8', '5')
        e = Rational('-7', '-4')
        f = Rational('-5', '-6')
        g = Rational('8', '-9')
        h = Rational('5', '-4')
        result1 = a.__add__(b)
        result2 = c.__add__(d)
        result3 = e.__add__(f)
        result4 = g.__add__(h)
        self.assertEqual(result1, Rational('25', '6'))
        self.assertEqual(result2, Rational('-44', '15'))
        self.assertEqual(result3, Rational('31', '12'))
        self.assertEqual(result4, Rational('-77', '36'))
    
    def test_Exception(self)
        r = Rational()
        self.assertRaises(ValueError, r.__add__(True), "Booleans not allowed")


    def test_AddOfTwoIntegerRationalNumbers(self):
        a = Rational('3', '1')
        b = Rational('5', '1')
        c = Rational('-4', '1')
        d = Rational('6', '1')
        e = Rational('4', '1')
        f = Rational('-3', '1')
        g = Rational('-9', '1')
        h = Rational('-8', '1)')
        result1 = a.__add__(b)
        result2 = c.__add__(d)
        result3 = e.__add__(f)
        result4 = g.__add__(h)
        self.assertEqual(result1, Rational('8', '1'))
        self.assertEqual(result2, Rational('2', '1'))
        self.assertEqual(result3, Rational('1', '1'))
        self.assertEqual(result4, Rational('-17', '1'))

    def test_AdditionByZero(self):
        a = Rational('4', '3')
        b = Rational('0', '1')
        c = Rational('-7', '4')
        d = Rational('0', '-5')
        result1 = a.__add__(b)
        result2 = c.__add__(d)
        self.assertEqual(result1, Rational('4', '3'))
        self.assertEqual(result2, Rational('-7', '4'))

if __name__ == '__main__':
    unittest.main()
