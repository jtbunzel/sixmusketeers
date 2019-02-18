import unittest
from Rational import *

class TestStr(unittest.TestCase):
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

if __name__ == '__main__':
	unittest.main()