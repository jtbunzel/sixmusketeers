import unittest as ut


class TestLogin(ut):
    def test_correct_login(self):
        # assume user exists
        a=app()
        result = a.command('login username password')
        self.assertEqual(result, 'Login successful.')

    def test_login_incorrect_password(self):
        # assume user exists
        a = app()
        result = a.command('login username notthepassword')
        self.assertEqual(result, 'Login unsuccessful. Password is incorrect.')

    def test_login_incorrect_username(self):
        # assume user exists
        a = app()
        result = a.command('login nottheusername password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_login_username_password_incorrect(self):
        # assume user exists
        a = app()
        result = a.command('login nottheusername notthepassword')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_login_user_does_not_exist(self):
        # assume user does not exist in system
        a = app()
        result = a.command('login username password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')


if __name__ == '__main__':
    ut.main()
