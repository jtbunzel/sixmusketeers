import unittest


class MyTestCase(unittest.TestCase):
    def test_userCanCreate(self):
        a = app();
        result = a.command("create account")
        # will fail if :
        #               - user is not (Supervisor or Secretary)
        #               - user is not logged in at all
        self.assertEqual(result, "logged in and authorized to create")

    def test_username(self):
        a = app()
        a.command('create account')
        result = a.command('user1')
        # Will fail if user name is already in database
        self.assertEqual(result, "name successfully created")

    def test_userpassword(self):
        a = app()
        a.command('create account')
        a.command('user1')
        result = a.command("pass123")
        self.assertEqual(result, "result successfully created")

    def test_name(self):
        a = app()
        a.command('create account')
        a.command('user1')
        result = a.command("will smith")
        # will fail
        # - if name format is not valid
        # - or entered first name only
        self.assertEqualt(result, "Name format is valid")

    def test_userrole(self):
        a = app()
        a.command('create account')
        a.command('user1')
        a.command("will smith")
        result = a.command('TA')
        # Will fail if no role is matched
        self.assertEqual(result, 'role is valid')

    def test_phoneNumber(self):
        a = app()
        a.command('create account')
        a.command('user1')
        a.command("will smith")
        a.command('TA')
        result = a.command('phone number')
        self.assertEqual(result, "phone number valid")

    def test_email(self):
        a = app()
        a.command('create account')
        a.command('user1')
        a.command("will smith")
        a.command('TA')
        # email must at least contains @
        result = a.command('aaabb@uwm.edu')
        self.assertEqual(result, "email is valid")

    def test_phoneNumber(self):
        a = app()
        a.command('create account')
        a.command('user1')
        a.command("will smith")
        a.command('TA')
        a.command('phone number')
        a.command('aaabb@uwm.edu')
        result = a.command('home address')
        self.assertEqual(result, "home address is valid")


    def test_createCourse(self):
        a = app()
        result = a.command('create course')
        # will fail if:
        #       - user is logged in
        #       - user is not authorized to create
        #       must be(Supervisor/ secretary)
        self.assertEqual(result, "course created")

    def test_assignCourseNumber(self):
        a = app()
        a.command('create course')
        result = a.command('CS395')
        # fails if course is available
        self.assertEqual(result, "course assigned a number")

    def test_assignCourseInstructor(self):
        a = app()
        a.command('create course')
        a.command('CS395')
        result = a.command('Batman')
        # will fail of instructor is not in school
        self.assertEqual(result, 'instructor assigned')

    def test_numberOfLabSections(self):
        a = app()
        a.command('create course')
        a.command('CS395')
        a.command('Batman')
        result = a.command('4')
        # will fail if format is wrong
        self.assertEqual(result, 'labs created')

    def test_assignTAs(self):
        a = app()
        a.command('create course')
        a.command('CS395')
        a.command('Batman')
        a.command('4')
        result = a.command('Robin, CatWoman')
        # will fail if names are not in school
        self.assertEqual(result, 'TAs assigned')


if __name__ == '__main__':
    unittest.main()
