import unittest
from App import *

a = App


class testTa(unittest.Testcase):
    def test_edit_full_name(self, other):
        result = a.edit(self, other)
        self.assertEqual(self, result)

    def test_edit_address(self, other):
        result = a.edit(self, other)
        self.assertEqual(self, result)

    def test_edit_email(self, other):
        result = a.edit(self, other)
        self.assertEqual(self, result)

    def test_edit_phone_number(self, other):
        result = a.edit(self, other)
        self.assertEqual(self, result)

    def test_view_TA_assignments(self):
        result = a.assignments(self)
        self.assertTrue(result)

    def test_view_public_info(self):
        result = a.access(self)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
