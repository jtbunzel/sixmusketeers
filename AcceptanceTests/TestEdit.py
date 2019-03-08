import unittest as bk

class TestEdit(bk):
    a = app()
        # assume user exists
        # assume user is logged in
        # assume user is supervisor
        #assume user is administor
        # assume user is instructors and TAs

    def test_supervisorEditAccount(self):
        # assume user is supervisor
        result1 = a.command('edit TA account successfull')
        self.assertEqual(result1, 'edit successfully.')
            #can edit TA's account

        result2 = a.command('edit administors account successfull')
        self.assertEqual(result2, 'edit successfully.')
            # can edit administors account

        result3 = a.command('edit Student account successfull')
        self.assertEqual(result3, 'edit successfully.')
            # can edit students account
        result4 = a.command('edit Instructors account successfull')
        self.assertEqual(result4, 'edit successfully.')
            #can edit Instructors account

    def test_supervisorEditCourse(self):
        # assume user is supervisor
        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit successfully')
            # can edit courses

    def test_AdminEditAccount(self):
        # assume user is Admin
        result1 = a.command('edit TA account successfull')
        self.assertEqual(result1, 'edit successfully.')
            #can edit TA's account
        result2 = a.command('edit administor account successfull')
        self.assertEqual(result2, 'edit unsuccessfully.')
            # can edit administors account
        result3 = a.command('edit Student account successfull')
        self.assertEqual(result3, 'edit successfully.')
            # can edit Students Account
        result4 = a.command('edit Instructors account successfull')
        self.assertEqual(result4, 'edit successfully.')
            # can edit Instructors account

    def test_AdminEditCourse(self):
        # assume user is Admin
        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit successfully')
            # can edit courses

    def test_taEditAccount(self):
        # assume user is TA
        result1 = a.command('edit TA account successfull')
        self.assertEqual(result1, 'edit successfully.')
            #can edit TA's account
        result2 = a.command('edit administors account successfull')
        self.assertEqual(result2, 'edit unsuccessfully.')
            # cann't edit administors account
        result3 = a.command('edit Student account successfull')
        self.assertEqual(result3, 'edit unsuccessfully.')
            # cann't edit student's account
        result4 = a.command('edit Instructors account successfull')
        self.assertEqual(result4, 'edit unsuccessfully.')
            # cann't edit Instructors account


    def test_taEditCourse(self):
        # assume user is TA
        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit unsuccessfully')
            # can't  edit courses

    def test_instructorEditAccount(self):
        # assume user is Instructors
        result1 = a.command('edit TA account successfull')
        self.assertEqual(result1, 'edit successfully.')
            #cann't edit TA's account
        result2 = a.command('edit administors account successfull')
        self.assertEqual(result2, 'edit unsuccessfully.')
            # cann't edit administors account
        result3 = a.command('edit Student account successfull')
        self.assertEqual(result3, 'edit unsuccessfully.')
            # cann't edit students account
        result4 = a.command('edit Instructors account successfull')
        self.assertEqual(result4, 'edit unsuccessfully.')
            # can edit Instructors account


    def test_instructorsEditCourse(self):
        # assume user is Instructors
        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit unsuccessfully')
            # can't edit courses

if __name__ == '__main__':

    bk.main()
