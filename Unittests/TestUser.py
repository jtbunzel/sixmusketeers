import unittest
from Skeleton_Classes.User import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User('wheelerg', '1234')
        self.user.set_full_name('Grant Wheeler')
        self.user.set_address('3200 N. Cramer St. Milwaukee, WI 53211')
        self.user.set_email('wheelerg@uwm.edu')
        self.user.set_phone_number('4148857236')

    def test_constructor(self):
        user = User('patel59', 'iamawesome')
        username = user.username
        password = user.password
        self.assertEqual(username, 'patel59')
        self.assertEqual(password, 'iamawesome')

    def test_get_username(self):
        result = self.user.get_username()
        self.assertEqual(result, 'wheelerg')

    def test_get_password(self):
        result = self.user.get_password()
        self.assertEqual(result, '1234')

    def test_get_full_name(self):
        result = self.user.get_full_name()
        self.assertEquals(result, 'Grant Wheeler')

    def test_get_address(self):
        result = self.user.get_address()
        self.assertEqual(result, '3200 N. Cramer St. Milwaukee, WI 53211')

    def test_get_phone_number(self):
        result = self.user.get_phone_number()
        self.assertEqual(result, '4148857236')

    def test_get_email(self):
        result = self.user.get_email()
        self.assertEqual(result, 'wheelerg@uwm.edu')

    def test_set_username(self):
        self.user.set_username('gwheeler')
        result = self.user.get_username()
        self.assertEquals(result, 'gwheeler')

    def test_set_password(self):
        self.user.set_password('4321')
        result = self.user.get_password()
        self.assertEquals(result, '4321')

    def test_set_full_name(self):
        self.user.set_full_name('Gina Wheeler')
        result = self.user.get_full_name()
        self.assertEquals(result, 'Gina Wheeler')

    def test_set_address(self):
        self.user.set_address('3400 N. Maryland Av. Milwaukee, WI 53211')
        result = self.user.get_address()
        self.assertEquals(result, '3400 N. Maryland Av. Milwaukee, WI 53211')

    def test_set_phone_number(self):
        self.user.set_phone_number('4145882300')
        result = self.user.get_phone_number()
        self.assertEquals(result, '4145882300')

    def test_set_email(self):
        self.user.set_email('gwheeler@uwm.edu')
        result = self.user.get_email()
        self.assertEquals(result, 'gwheeler@uwm.edu')


if __name__ == '__main__':
    unittest.main()
