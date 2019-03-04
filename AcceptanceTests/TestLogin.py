import unittest as ut


class TestLogin(ut):
    def test_correctlogin(self):
        # assume user exists
        result = a.command('login username password')
        self.assertEqual(result, 'Login successful.')

    def test_LoginIncorrectPassword(self):
        # assume user exists
        a = app()
        result = a.command('login username notthepassword')
        self.assertEqual(result, 'Login unsuccessful. Password is incorrect.')

    def test_loginincorrectusername(self):
        # assume user exists
        a = app()
        result = a.command('login nottheusername password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_loginusernamepasswordincorrect(self):
        # assume user exists
        a = app()
        result = a.command('login nottheusername notthepassword')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_loginuserdoesnotexist(self):
        # assume user does not exist in system
        a = app()
        result = a.command('login username password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')


if __name__ == '__main__':
    ut.main()
