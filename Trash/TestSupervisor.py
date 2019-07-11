import unittest
from Trash.Supervisor import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.supervisor = Supervisor('hunterg', 'passwerd')
        self.supervisor.set_full_name('Hunter Green')
        self.supervisor.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.supervisor.set_email('hunterg@uwm.edu')
        self.supervisor.set_phone_number('414-569-8784')


    def test_constructor(self):
        test_supervisor = Supervisor('hunterg', 'passwerd')
        result = test_supervisor.get_username()
        expected = 'hunterg'
        self.assertEquals(result, expected)
        result = test_supervisor.get_password()
        expected = 'passwerd'
        self.assertEquals(result, expected)

    def test_str(self):
        self.setUp()
        result = self.supervisor.__str__()
        expected = 'Hunter Green\nAdministrator\nhunterg\npasswerd\n1107 N. Oregon St.\nhunterg@uwm.edu\n414-569-8784'
        self.assertEquals(result, expected)

    def test_get_public_contact_info(self):
        self.setUp()
        result = self.supervisor.get_public_contact_info()
        expected = 'Hunter Green\nAdministrator\nhunterg@uwm.edu'
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()

