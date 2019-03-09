import unittest
from AcceptanceTests import App


class MyTestCase(unittest.TestCase):
    def test_logout(self):
        # assume user logged in
        a = App()
        result = a.command('logout')
        self.assertEquals(result, 'Logout successful.')

    def test_logout_attempt_assign_afterwards(self):
        # assume user logged in
        a = App()
        result = a.command('logout')
        self.assertEquals(result, 'Logout successful.')
        result = a.command('assign TA')
        self.assertEquals(result, 'Command unavailable. No user logged in.')

    def test_logout_login_again(self):
        # assume user logged in
        a = App()
        result = a.command('logout')
        self.assertEquals(result, 'Logout successful.')
        result = a.command('login username password')
        self.assertEquals(result, 'Login successful.')

    def test_logout_login_as_other_user(self):
        # assume user logged in as Supervisor(username)
        # assume otherusername exists in the system and is a TA
        a = App()
        result = a.command('logout')
        self.assertEquals(result, 'Logout successful')
        result = a.command('login otherusername otherpassword')
        self.assertEquals(result, 'Login successful.')
        result = a.command('assign TA')
        self.assertEquals(result, 'Command unavailable.')


if __name__ == '__main__':
    unittest.main()
