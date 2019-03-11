import unittest as bk


class TestEdit(bk):
    # assume user exist
    # assume user is logged in
    # assume user is supervisor/admin/ instructors/TA
    # fail:
    #       if format for particular title is not valid
    #       if Instructors attempt to edit any other user except themself
    #       if TA attempt to edit any other users except themself
    #       if Admin attmpt to edit:- supervisor and another admin

    def test_editPhoneNumber(self):
        a = App()
        result= a.command('edit phoneNumber')
            # will edit phone Number
        self.assertEqual(result, 'edit phone number successfully')

    def test_editUserName(self):
        a = App()
        result= a.command('edit User name')
        # will edit username
        self.assertEqual(result, 'edit user name successfully')

    def test_editPassword(self):
        a = App()
        result= a.command('edit password')
        #will edit password
        self.assertEqual(result, 'successful editing password')

    def test_editAddress(self):
        a = App()
        result= a.command('edit address')
        # edit address
        self.assertEqual(result, 'address successfully edited')

    def test_editEmailaddress(self):
        a = App()
        result= a.command('edit email address')
            # will fail if email address doesnot have @
        self.assertEqual(result, 'edit email address successfully')

    def test_editName(self):
        a = App()
        result= a.command('edit firstName')
        self.assertEqual(result,'edit first name successfully')
        result = a.command('edit lastName')
        self.assertEqual(result, 'edit last name successfully')


    # will fail :
    #            will fail if TA/Instructor attempt to edit anything related to course
    def test_editCourse(self):
        a = App()
        result= a.command('edit Course')
        # will fail:
        #           if TA/Instructors attempt to edit course
        #           if course doesnot exist
        self.assertEqual(result,'course edited successfully')

    def test_editCourseNumber(self):
        a = App()
        a.command('course edited')
        result = a.command('cs361')
        self.assertEqual(result,'edit course number successfully')

    def test_editCourse_lab_section(self):
        a = App()
        a.command('course edited')
        a.command('cs361')
        result= a.command('700')
        self.assertEqual(result,'edit lab section successfully')

    def test_editCourseforInstructor(self):
        a = App()
        a.command('course edited')
        a.command('cs361')
        a.command('700')
        result= a.command('Name of the Instructor')
        # will fail if instructor does not exit
        self.assertEqual(result, 'Instructor for course is edited successfully')

    def test_editCourseforTA(self):
        a = App()
        a.command('course edited')
        a.command('cs361')
        a.command('700')
        a.command('Name of the Instructor')
        result= a.command('Name of the TA')
        # will fail if TA does not exit
        self.assertEqual(result,'edit TA for course successfully')


if __name__ == '__main__':

    bk.main()
