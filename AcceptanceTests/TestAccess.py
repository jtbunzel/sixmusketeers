import unittest


class TestAccess(unittest.TestCase):
    def test_userCanAccess(self):
        a = app()
        result = a.command("access account")
        # will fail if :
        #               - user is not (Supervisor or Secretary)
        #               - user is not logged in at all
        #               - administrator tried to access supervisor information
        self.assertEqual(result, "logged in and authorized to access")

    def test_accessusername(self):
        a = app()
        a.command('access account')
        result = a.command('user1')
        # Will fail if user name isn't in the database
        self.assertEqual(result, "name successfully accessed")


    def test_accessname(self):
        a = app()
        a.command('access account')
        a.command('user1')
        result = a.command("will smith")
        # will fail
        # - if name format is not valid
        # - or entered first name only
        self.assertEqualt(result, "name is access")

    def test_accessrole(self):
        a = app()
        a.command('access account')
        a.command('user1')
        a.command("will smith")
        result = a.command('TA')
        # Will fail if no role is matched
        self.assertEqual(result, 'role is accessed')

    def test_accessphoneNumber(self):
        a = app()
        a.command('access account')
        a.command('user1')
        a.command("will smith")
        a.command('TA')
        result = a.command('phone number')
        self.assertEqual(result, "phone number is accessed")

    def test_accessemail(self):
        a = app()
        a.command('access account')
        a.command('user1')
        a.command("will smith")
        a.command('TA')
        # email must at least contains @
        result = a.command('aaabb@uwm.edu')
        self.assertEqual(result, "email is accessed")

    def test_accesshomeaddress(self):
        a = app()
        a.command('access account')
        a.command('user1')
        a.command("will smith")
        a.command('TA')
        a.command('phone number')
        a.command('aaabb@uwm.edu')
        result = a.command('home address')
        self.assertEqual(result, "home address is accessed")


    def test_createCourse(self):
        a = app()
        result = a.command('access course')
        # will fail if:
        #       - user is logged in
        #       - user is not authorized to create
        #       must be(Supervisor/ secretary)
        self.assertEqual(result, "course access")

    def test_accessCourseNumber(self):
        a = app()
        a.command('access course')
        result = a.command('CS361')
        # fails if course isn't available
        self.assertEqual(result, "course number is accessed")

    def test_accessCourseInstructor(self):
        a = app()
        a.command('access course')
        a.command('CS361')
        result = a.command('Rock')
        # will fail of instructor is not in school
        self.assertEqual(result, "course instructor is accessed")

    def test_accessnumberOfLabSections(self):
        a = app()
        a.command('create course')
        a.command('CS361')
        a.command('Rock')
        result = a.command('4')
        # will fail if format is wrong
        self.assertEqual(result, 'total lab section are accessed')

    def test_accessTAs(self):
        a = app()
        a.command('create course')
        a.command('CS361')
        a.command('Rock')
        a.command('4')
        result = a.command('Robin, Jack')
        # will fail if names are not in school
        self.assertEqual(result, 'TAs are accessed ')


if __name__ == '__main__':
    unittest.main()