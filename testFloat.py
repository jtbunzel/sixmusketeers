import unittest

from Rational import Rational

s1 = Rational(1,  2)
s2 = Rational(1, 0.00000000000000000000000000000001)
s3 = Rational(2.5, 2)
s4 = Rational(1, 0.5)
s5 = Rational("5", 4)
s6 = Rational(5, "4")
s7 = Rational(1, 99999999999999999999999999999999999)
s8 = Rational(True, 1)
s9 = Rational(1, False)


class TesSolver(unittest.TestCase):
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


