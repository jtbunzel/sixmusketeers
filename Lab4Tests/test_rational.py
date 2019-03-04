import unittest
from Lab4Tests.Rational import *

a7 = Rational(1, 1)
b7 = Rational(10, 20)
c7 = Rational(-5, -7)
d7 = Rational(3, -3)
e7 = Rational(-7, 7)
f7 = Rational(0, 1)
g7 = Rational(1, 99999999999999999999999999999999999)
h7 = Rational(1, 0.00000000000000000000000000000001)
s1 = Rational(1, 2)
s2 = Rational(1, 0.00000000000000000000000000000001)
s3 = Rational(2.5, 2)
s4 = Rational(1, 0.5)
s5 = Rational("5", 4)
s6 = Rational(5, "4")
s7 = Rational(1, 99999999999999999999999999999999999)
s8 = Rational(True, 1)
s9 = Rational(1, False)


class TestRational(unittest.TestCase):

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

    def test_Exception(self):
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
        d = Rational('-1,', '3')
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
        e = Rational('0', '0')
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

    def test_multiplyByOne(self):
        self.assertTrue(a7.__mul__(a7) == Rational(1, 1))
        self.assertTrue(a7.__mul__(b7) == Rational(10, 20))
        self.assertTrue(a7.__mul__(c7) == Rational(-5, -7))
        self.assertTrue(a7.__mul__(d7) == Rational(3, -3))
        self.assertTrue(a7.__mul__(e7) == Rational(-7, 7))
        self.assertTrue(a7.__mul__(f7) == Rational(0, 1))
        self.assertTrue(a7.__mul__(g7) == Rational(1, 99999999999999999999999999999999999))
        self.assertTrue(a7.__mul__(h7) == Rational(1, 0.00000000000000000000000000000001))

    def test_multiplyByZero(self):
        self.assertTrue(f7.__mul__(a7) == Rational(0, 1))
        self.assertTrue(f7.__mul__(b7) == Rational(0, 20))
        self.assertTrue(f7.__mul__(c7) == Rational(0, -7))
        self.assertTrue(f7.__mul__(d7) == Rational(0, -3))
        self.assertTrue(f7.__mul__(e7) == Rational(0, 7))
        self.assertTrue(f7.__mul__(f7) == Rational(0, 1))
        self.assertTrue(f7.__mul__(g7) == Rational(0, 99999999999999999999999999999999999))
        self.assertTrue(f7.__mul__(h7) == Rational(0, 0.00000000000000000000000000000001))

    def test_multiplyBySelf(self):
        self.assertTrue(a7.__mul__(a7) == Rational(1, 1))
        self.assertTrue(b7.__mul__(b7) == Rational(100, 400))
        self.assertTrue(c7.__mul__(c7) == Rational(25, 49))
        self.assertTrue(d7.__mul__(d7) == Rational(9, 9))
        self.assertTrue(e7.__mul__(e7) == Rational(49, 49))
        self.assertTrue(f7.__mul__(f7) == Rational(0, 1))
        self.assertTrue(
            g7.__mul__(g7) == Rational(1, 9999999999999999999999999999999999800000000000000000000000000000000001))

    def test_multiplyByNegativeDenominator(self):
        self.assertTrue(d7.__mul__(a7) == Rational(3, -3))
        self.assertTrue(d7.__mul__(b7) == Rational(30, -60))
        self.assertTrue(d7.__mul__(c7) == Rational(-15, 21))
        self.assertTrue(d7.__mul__(d7) == Rational(9, 9))
        self.assertTrue(d7.__mul__(e7) == Rational(-21, -21))
        self.assertTrue(d7.__mul__(f7) == Rational(0, -3))
        self.assertTrue(d7.__mul__(g7) == Rational(3, -299999999999999999999999999999999997))

    def test_multiplyByNegativeNumerator(self):
        self.assertTrue(e7.__mul__(a7) == Rational(-7, 7))
        self.assertTrue(e7.__mul__(b7) == Rational(-70, 140))
        self.assertTrue(e7.__mul__(c7) == Rational(35, -49))
        self.assertTrue(e7.__mul__(d7) == Rational(-21, -21))
        self.assertTrue(e7.__mul__(e7) == Rational(49, 49))
        self.assertTrue(e7.__mul__(f7) == Rational(0, 7))
        self.assertTrue(e7.__mul__(g7) == Rational(-7, 699999999999999999999999999999999993))

    def test_multiplyByNegativeRational(self):
        self.assertTrue(c7.__mul__(a7) == Rational(-5, -7))
        self.assertTrue(c7.__mul__(b7) == Rational(-50, -140))
        self.assertTrue(c7.__mul__(c7) == Rational(25, 49))
        self.assertTrue(c7.__mul__(d7) == Rational(-15, 21))
        self.assertTrue(c7.__mul__(e7) == Rational(35, -49))
        self.assertTrue(c7.__mul__(f7) == Rational(0, -7))
        self.assertTrue(c7.__mul__(g7) == Rational(-5, -699999999999999999999999999999999993))

    def test_DivisionBySelf(self):
        a = Rational(7, 2)
        b = Rational(7, 2)
        result = a.__div__(b)
        self.assertTrue(result == Rational(1, 1))

    def test_DivisionOfTwoDifferentRationalNumbers(self):
        a = Rational(2, 3)
        b = Rational(5, 8)
        result = a.__div__(b)
        self.assertTrue(result == Rational(16, 15))

    def test_DivisionOfTwoIntegers(self):
        a = Rational(3, 1)
        b = Rational(5, 1)
        result = a.__div__(b)
        self.assertTrue(result == Rational(3, 5))

    def test_DivisionByZero(self):
        a = Rational(4, 3)
        b = Rational(0, 1)
        with self.assertRaises(ZeroDivisionError):
            a.__div__(b)

    def test_ReductionOfAnswer(self):
        a = Rational(2, 3)
        b = Rational(3, 4)
        result = a.__div__(b)
        self.assertTrue(result == Rational(1, 2))

    default = Rational()
    neg_num = Rational(-1, 3)
    neg_den = Rational(1, -2)
    neg_both = Rational(-1, -2)
    whole_num = Rational(2)

    def test_str_default(self):
        self.assertEqual(str(self.default), "0/1")

    def test_str_neg_num(self):
        self.assertEqual(str(self.neg_num), "-1/3")

    def test_str_neg_den(self):
        self.assertEqual(str(self.neg_den), "1/-2")

    def test_str_neg_both(self):
        self.assertEqual(str(self.neg_both), "-1/-2")

    def test_str_whole_num(self):
        self.assertEqual(str(self.whole_num), "2/1")

    def test_float_denm(self):
        self.assertGreaterEqual(s1.d, 0, "denominator can't be negative")
        self.assertFalse(s1.d < 0, "denominator can't be negative")

    def test_float_type(self):
        self.assertEqual(type(s1.__float__()), type(1.1), "Float type wrong")
        # 1/0 undefined
        with self.assertRaises(TypeError):
            s2.__float__()
        self.assertEqual(type(s3.__float__()), type(1.1), "Float type wrong")
        self.assertEqual(type(s4.__float__()), type(1.1), "Float type wrong")
        with self.assertRaises(TypeError):
            s5.__float__()
        with self.assertRaises(TypeError):
            s6.__float__()
        with self.assertRaises(TypeError):
            s8.__float__()
        with self.assertRaises(TypeError):
            s9.__float__()

    def test_float_result(self):
        self.assertEqual(s3.__float__(), 1.25, "wrong result")
        self.assertEqual(s1.__float__(), 0.5, "wrong result")
        self.assertEqual(s4.__float__(), 2, "wrong result")
        self.assertEqual(s7.__float__(), 0.0, "denominator is really big so value is 0")

    def test_AddATrueBool(self):
        b = Rational()
        self.assertRaises(TypeError, b.__add__(True))

    def test_AddAFalseBool(self):
        b = Rational()
        self.assertRaises(TypeError, b.__add__(False))

    def test_AddAStr(self):
        s = Rational()
        self.assertRaises(TypeError, s.__add__("String"))


if __name__ == '__main__':
    unittest.main()