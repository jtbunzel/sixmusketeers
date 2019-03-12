import unittest as ut
#The import statements will be dealt with later


class MyTestCase(ut.TestCase):
    def setUp(self):
        pass

    def test_CorrectLogin(self):
        #assume user exists as TA
        a = app()
        result = a.command('login username password')
        self.assertEqual(result, 'Login successful.')

    def test_LoginIncorrectPassword(self):
        #assume user exists as TA
        a = app()
        result = a.command('login username notthepassword')
        self.assertEqual(result, 'Login unsuccessful. Password may be incorrect.')

    def test_LoginIncorrectUsername(self):
        #assume user exists as TA
        a = app()
        result = a.command('login nottheusername password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_LoginUsernamePasswordIncorrect(self):
        # assume user exists as TA
        a = app()
        result = a.command('login nottheusername notthepassword')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_LoginUserDoesNotExist(self):
        #assume user does not exist in system
        a = app()
        result = a.command('login username password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_Search


if __name__ == '__main__':
    unittest.main()
