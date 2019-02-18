import unittest
import Rational

self.default = Rational()
self.neg_num = Rational(-1, 3)
self.neg_den = Rational(1, -2)
self.neg_both = Rational(-1, -2)
self.whole_num = Rational(2)

class TestStr(unittest.TestCase):
	def test_str_default(self):
		self.assertEqual(str(self.default), "0/1")

	def test_str_neg_num(self):
		self.assertEqual(str(self.neg_num), "-1/3")

	def test_str_neg_den(self):
		self.assertEqual(str(self.neg_den), "-1/2")

	def test_str_neg_both(self):
		self.assertEqual(str(self.neg_both), "1/2")

	def test_str_whole_num(self):
		self.assertEqual(str(self.whole_num), "2/1")

if __name__ == '__main__':
	unittest.main()