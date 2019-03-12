import unittest
from Administrator import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.admin = Administrator('hunterg', 'passwerd')
        self.admin.set_full_name('Hunter Green')
        self.admin.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.admin.set_email('hunterg@uwm.edu')
        self.admin.set_phone_number('414-569-8784')

    def test_constructor(self):
        admin = Administrator('hunterg', 'passwerd')
        result = admin.get_username()
        expected = 'hunterg'
        self.assertEquals(result, expected)
        result = admin.get_password()
        expected = 'passwerd'
        self.assertEquals(result, expected)

    def test_str(self):
        self.setUp()
        result = self.admin.__str__()
        expected = 'Hunter Green\nAdministrator\nhunterg\npasswerd\n1107 N. Oregon St.\nhunterg@uwm.edu\n414-569-8784'
        self.assertEquals(result, expected)

    def test_get_public_contact_info(self):
        self.setUp()
        result = self.admin.get_public_contact_info()
        expected = 'Hunter Green\nAdministrator\nhunterg@uwm.edu'
        self.assertEquals(result, expected)






if __name__ == '__main__':
    unittest.main()
