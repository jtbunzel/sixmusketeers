import unittest
from Skeleton_Classes.Database import *
from Skeleton_Classes.Course import *
from Skeleton_Classes.Supervisor import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account = Supervisor('hunterg', 'passwerd')
        self.account.set_full_name('Hunter Green')
        self.account.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.account.set_email('hunterg@uwm.edu')
        self.account.set_phone_number('414-569-8784')

        self.course = Course("Math", "MTH", "Bob", "101")

    def test_read_account(self):
        self.setUp()
        result = self.read()
        self.assertEquals(result, self.account)

    def test_read_course(self):
        self.setUp()
        result = self.read()
        self.assertEquals(result, self.course)

    def test_write_account(self):
        self.setUp()
        expected = self.account

        self.write()
        result = self.read()
        self.assertEquals(result, expected)

    def test_write_course(self):
        self.setUp()
        expected = self.course

        self.write()
        result = self.read()
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()