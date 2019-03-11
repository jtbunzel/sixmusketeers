import unittest
from User import *
import App

a = App


class testTa(unittest.Testcase):
    def test_edit_full_name(self, other):
        result = a.command(self, other)
        self.assertEqual(self, result)

    def test_edit_address(self, other):
        result = a.command(self, other)
        self.assertEqual(self, result)

    def test_edit_email(self, other):
        result = a.command(self, other)
        self.assertEqual(self, result)

    def test_edit_phone_number(self, result):
        result = a.command(self, other)
        self.assertEqual(self, result)

    def test_view_TA_assignments(self):
        result = a.command(self)
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
