from unittest import TestCase
from Rational import Rational

s1 = Rational(1,  2)
s3 = Rational(2.5, 2)
s4 = Rational(1, 0.5)


class TesSolver(TestCase):
    def test_float_denm(self):
        self.assertGreaterEqual(s1.d, 0, "denominator can't be negative")
        self.assertFalse(s1.d < 0, "denominator can't be negative")

    def test_float_type(self):
        self.assertEqual(type(s1.__float__()), type(1.1), "Float type wrong")
        self.assertEqual(type(s3.__float__()), type(1.1), "Float type wrong")
        self.assertEqual(type(s4.__float__()), type(1.1), "Float type wrong")

    def test_float_result(self):
        self.assertEqual(s3.__float__(), 1.25, "wrong result")
        self.assertEqual(s1.__float__(), 0.5, "wrong result")
        self.assertEqual(s4.__float__(), 2, "wrong result")


