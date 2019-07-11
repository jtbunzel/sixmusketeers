import unittest
from App import *


class MyTestCase(unittest.TestCase):
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
        a.command('user0')
        a.command("Bijaya khanal")
        a.command('TA')
        result = a.command('phone number')
        self.assertEqual(result, "phone number is accessed")

    def test_accessemail(self):
        a = app()
        a.command('access account')
        a.command('user0')
        a.command("Bijaya khanal")
        a.command('TA')
        # email must at least contains @
        result = a.command('bkhanal.edu')
        self.assertEqual(result, "email is accessed")

    def test_accesshomeaddress(self):
        a = app()
        a.command('access account')
        a.command('user0')
        a.command("Bijaya khanal")
        a.command('TA')
        a.command('phone number')
        a.command('bkhanal@uwm.edu')
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

    def test_assign_TA_to_lab_section_as_instructor_use_name(self):
        # Assume user logged in as instructor
        # Assume TA and lab section exist
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 Section 801.')

    def test_assign_TA_to_lab_section_as_instructor_use_username(self):
        # Assume user logged in as instructor
        # Assume TA and lab section exist
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'wheelerg assigned to CS361 Section 801.')

    def test_assign_TA_not_assigned_to_course(self):
        # Assume user logged in as instructor
        # Assume TA exists
        # Assume TA NOT assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'TA not assigned to this course.')

    def test_assign_TA_to_nonexistant_lab_section(self):
        # Assume user logged in as instructor
        # Assume TA exists
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respond_to_prompt('847')
        self.assertEquals(result, 'Lab Section does not exist.')

    def test_assign_TA_to_course_and_lab_as_supervisor_use_username(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'wheelerg assigned to CS361 Section 801.')

    def test_assign_TA_to_course_and_lab_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 Section 801.')

    def test_assign_TA_to_course_as_grader_as_supervisor_use_name(self):
        # Assume user logged in is an supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('Grader')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 as Grader.')

    def test_assign_TA_to_course_as_supervisor_use_name(self):
        # Assume user logged in is an supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('N/A')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361')

    def test_assign_TA_to_nonexistant_course_as_supervisor(self):
        # Assume user logged in as supervisor
        # Assume TA exists
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS575')
        self.assertEqual(result, 'Course does not exist.')

    def test_assign_nonexistant_TA_as_supervisor(self):
        # Assume user logged in as supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or username?: ')
        result = a.respond_to_prompt('Kurt Cobain')
        self.assertEquals(result, 'TA does not exist.')

    # assume user exists
    # assume user is logged in
    # assume user an instructor or TA
    def test_emptyAssignmentsList(self):
        result = a.command('courses')
        self.assertEqual(result, 'No assignments exist')

    def test_viewAllAssignments(self):
        result = a.command('courses')
        self.assertEqual(result, 'TA: Assignments: ')

    def test_assign__TA_as_TA(self):
        # Assume user logged in as TA
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_instructor_as_TA(self):
        # Assume user logged in as TA
        a = App()
        result = a.command('assign Instructor')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_TA_as_supervisor(self):
        # Assume user logged in as supervisor
        a = App()
        result = a.command('assign Instructor')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_instructor_as_supervisor(self):
        # Assume user logged in as supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_instructor_as_instructor(self):
        # Assume user logged in as instructor
        a = App()
        result = a.command('assign Instructor')
        self.assertEquals(result, 'Command not authorized.')

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

    def test_invalidPermission(self):
        a = app()
        result = a.command("delete dataType name")
        # the user does not have the correct role

        self.assertEqual(result, "user does not have permission")

    def test_invalidDataType(self):
        a = app()
        result = a.command("delete dataType name")
        # the data type is not valid

        self.assertEqual(result, "the datatype is not class or acocunt")

    def test_invalidName(self):
        a = app()
        result = a.command("delete dataType name")
        # the data does not exist

        self.assertEqual(result, "the data does not exist")

    def test_validDataType_InvalidName(self):
        a = app()
        result = a.command("delete dataType name")
        # the datatype is valid but the data does not exist

        self.assertEqual(result, "there is no data under this name")

    def test_validEntry(self):
        a = app()
        result = a.command("delete dataType name")
        # the datatype is either class or account
        # the data exists

        self.assertEqual(result, "data deleted suggessfully")

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
        result = a.command('edit phoneNumber')
        # will edit phone Number
        self.assertEqual(result, 'edit phone number successfully')

    def test_editUserName(self):
        a = App()
        result = a.command('edit User name')
        # will edit username
        self.assertEqual(result, 'edit user name successfully')

    def test_editPassword(self):
        a = App()
        result = a.command('edit password')
        # will edit password
        self.assertEqual(result, 'successful editing password')

    def test_editAddress(self):
        a = App()
        result = a.command('edit address')
        # edit address
        self.assertEqual(result, 'address successfully edited')

    def test_editEmailaddress(self):
        a = App()
        result = a.command('edit email address')
        # will fail if email address doesnot have @
        self.assertEqual(result, 'edit email address successfully')

    def test_editName(self):
        a = App()
        result = a.command('edit firstName')
        self.assertEqual(result, 'edit first name successfully')
        result = a.command('edit lastName')
        self.assertEqual(result, 'edit last name successfully')

    # will fail :
    #            will fail if TA/Instructor attempt to edit anything related to course
    def test_editCourse(self):
        a = App()
        result = a.command('edit Course')
        # will fail:
        #           if TA/Instructors attempt to edit course
        #           if course doesnot exist
        self.assertEqual(result, 'course edited successfully')

    def test_editCourseNumber(self):
        a = App()
        a.command('course edited')
        result = a.command('cs361')
        self.assertEqual(result, 'edit course number successfully')

    def test_editCourse_lab_section(self):
        a = App()
        a.command('course edited')
        a.command('cs361')
        result = a.command('700')
        self.assertEqual(result, 'edit lab section successfully')

    def test_editCourseforInstructor(self):
        a = App()
        a.command('course edited')
        a.command('cs361')
        a.command('700')
        result = a.command('Name of the Instructor')
        # will fail if instructor does not exit
        self.assertEqual(result, 'Instructor for course is edited successfully')

    def test_editCourseforTA(self):
        a = App()
        a.command('course edited')
        a.command('cs361')
        a.command('700')
        a.command('Name of the Instructor')
        result = a.command('Name of the TA')
        # will fail if TA does not exit
        self.assertEqual(result, 'edit TA for course successfully')

    def test_invalidPermission(self):
        a = app()
        result = a.command("information name")
        # the user does not have the correct role
        # must be a TA, instructor, administrator, or a supervisor

        self.assertEqual(result, "user does not have permission")

    def test_invalidName(self):
        a = app()
        result = a.command("information name")
        # user has permission
        # the account does not exist

        self.assertEqual(result, "the data does not exist")

    def test_validEntry(self):
        a = app()
        result = a.command("information name")
        # user has permission
        # the account exists

        self.assertEqual(result, "information returned successfully")

    def test_correct_login(self):
        # assume user exists
        a = App()
        result = a.command('login username password')
        self.assertEqual(result, 'Login successful.')

    def test_login_incorrect_password(self):
        # assume user exists
        a = App()
        result = a.command('login username notthepassword')
        self.assertEqual(result, 'Login unsuccessful. Password is incorrect.')

    def test_login_incorrect_username(self):
        # assume user exists
        a = App()
        result = a.command('login nottheusername password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_login_username_password_incorrect(self):
        # assume user exists
        a = App()
        result = a.command('login nottheusername notthepassword')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

    def test_login_user_does_not_exist(self):
        # assume user does not exist in system
        a = App()
        result = a.command('login username password')
        self.assertEqual(result, 'Login unsuccessful. User not found.')

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

    # assume user exists
    # assume user is logged in
    # assume sender are Supervsiro/Admin/Instructor

    def test_message(self):
        # assume message is not empty
        # assume receiver has UWm email
        a = App
        result = a.command('sending message ')
        # will fail:
        #           if sent to non wum email address
        #           if email doesn't exit
        #           if TA attempts to send notification
        self.assertEqual(result, 'Notify successfully')

    def test_emptyMessage(self):
        # assume receiver has UWm email
        a = App()
        result = a.command('sending empty message')
        self.assertEqual(result, 'cannot notify empty message')

    def test_uwmemail(self):
        a = App()
        # assume message is not empty
        result = a.command('sending message to uwm email')
        self.assertEqual(result, 'Notify successfully')

    def test_nonuwmemail(self):
        # assume message is not empty
        a = App()
        result = a.command('sending message to non-uwm email')
        # fail:- non uwm email
        self.assertEqual(result, 'notify unsuccessful, invalid email address')

    def test_TA_as_notifer(self):
        a = App()
        # assume message is not empty
        # assume email address is valid
        result = a.command('TA sending message')
        self.assertEqual(result, 'not authorized to send notification')


if __name__ == '__main__':
    unittest.main()
