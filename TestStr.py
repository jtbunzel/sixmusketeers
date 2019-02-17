import unittest
import Rational

class TestStr(unittest.TestCase):
	def test_str_default(self):
		self.assertEqual(str(Rational()), "0/1")

	def test_str_neg_num(self):
		self.assertEqual(str(Rational(-1, 3)), "-1/3")

	def test_str_neg_den(self):
		self.assertEqual(str(Rational(1, -2)), "-1/2")

	def test_str_neg_both(self):
    	self.assertEqual(str(Rational(-1, -2)), "1/2")

	def test_str_whole_num(self):
		self.assertEqual(str(Rational(2)), "2/1")

if __name__ == '__main__':
    unittest.main()