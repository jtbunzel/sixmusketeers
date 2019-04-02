import unittest
from Skeleton_Classes.Administrator import Administrator
from Skeleton_Classes.Database import *
from Skeleton_Classes.Course import *
from Skeleton_Classes.Supervisor import *
from Skeleton_Classes.Course import Course
from Skeleton_Classes.Instructor import *
from Skeleton_Classes.LabSection import *
from Skeleton_Classes.Supervisor import *
from Skeleton_Classes.TA import *
from Skeleton_Classes.User import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.admin = Administrator('hunterg', 'passwerd')
        self.admin.set_full_name('Hunter Green')
        self.admin.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.admin.set_email('hunterg@uwm.edu')
        self.admin.set_phone_number('414-569-8784')

    def test_constructor(self):
        admin = Administrator('hunterg', 'passwerd')
        result = admin.get_username()
        expected = 'hunterg'
        self.assertEqual(result, expected)
        result = admin.get_password()
        expected = 'passwerd'
        self.assertEqual(result, expected)

    def test_str(self):
        self.setUp()
        result = self.admin.__str__()
        expected = 'Hunter Green\nAdministrator\nhunterg\npasswerd\n1107 N. Oregon St.\nhunterg@uwm.edu\n414-569-8784'
        self.assertEqual(result, expected)

    def test_get_public_contact_info(self):
        self.setUp()
        result = self.admin.get_public_contact_info()
        expected = 'Hunter Green\nAdministrator\nhunterg@uwm.edu'
        self.assertEqual(result, expected)

    def setUp(self):
        self.c1 = Course("Math", "MTH", "Bob", "101")

    def test_setup(self):
        self.assertEqual(self.c1.course_name, "Math")
        self.assertEqual(self.c1.course_type, "MTH")
        self.assertEqual(self.c1.course_instructor, "Bob")
        self.assertEqual(self.c1.course_code, "101")

    def test_getters(self):
        self.assertEqual(self.c1.get_name(), "Math")
        self.assertEqual(self.c1.get_type(), "MTH")
        self.assertEqual(self.c1.get_instructor(), "Bob")
        self.assertEqual(self.c1.get_number(), "101")

    def test_edit_course_instructor(self):
        self.edit_course_instructor("Rock")
        self.assertEqual(self.c1.course_instructor, "Rock")

    def test_add_lab(self):
        self.c1.add_lab("lab1")
        self.assertEqual(self.c1.lab_name[0], "lab1")

    def setUp(self):
        self.account = Supervisor('hunterg', 'passwerd')
        self.account.set_full_name('Hunter Green')
        self.account.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.account.set_email('hunterg@uwm.edu')
        self.account.set_phone_number('414-569-8784')

        self.course = Course("Math", "MTH", "Bob", "101")

    def test_read_account(self):
        self.setUp()
        result = self.read()
        self.assertEquals(result, self.account)

    def test_read_course(self):
        self.setUp()
        result = self.read()
        self.assertEquals(result, self.course)

    def test_write_account(self):
        self.setUp()
        expected = self.account

        self.write()
        result = self.read()
        self.assertEquals(result, expected)

    def test_write_course(self):
        self.setUp()
        expected = self.course

        self.write()
        result = self.read()
        self.assertEquals(result, expected)

    def setUp(self):
        self.instructor = Instructor('John', 'Doe')
        self.instructor.set_full_name('Johnny Cage')
        self.instructor.set_address('3208 N. Oakland Ave. Milwaukee WI 53211')
        self.instructor.set_email('JCage7@uwm.edu')
        self.instructor.add_course('Intro to Software Engineering')
        self.instructor.add_course('Intro to Artificial Intelligence')

    def test_constructor(self):
        username = self.instructor.get_username()
        self.assertEqual(username, 'John')
        pw = self.instructor.get_password()
        self.assertEqual(pw, 'Doe')

    def test_get_courses(self):
        result = self.instructor.get_courses
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Artificial Intelligence ')

    def test_add_courses(self):
        self.instructor.add_course('Intro to Computer Security')
        result = self.instructor.get_courses
        self.assertEqual(result,
                         'Intro to Software Engineering\nIntro to Artificial Intelligence\nIntro to Computer Security ')

    def test_remove_course(self):
        course_to_be_removed = 'Intro to Artificial Intelligence'
        self.instructor.remove_course(course_to_be_removed)
        result = self.instructor.get_courses
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Computer Security ')

    def test_get_public_contact_info(self):
        result = self.instructor.get_public_contact_info()
        self.assertEquals(result, 'Johnny Cage\nInstructor\nJCage7@uwm.edu')

    def setUp(self):
        self.lab = LabSection("801", "Henry", "12-3")

    def test_setUp(self):
        self.assertEqual(self.lab.lab_number, "801")
        self.assertEqual(self.lab.TA, "Henry")
        self.assertEqual(self.lab.lab_time, "12-3")

    def test_getters(self):
        self.assertEqual(self.lab.get_info(), "801, Henry, 12-3")

    def test_edit_lab_TA(self):
        self.lab.edit_lab_TA("John")
        self.assertEqual(self.lab.TA, "John")

    def test_edit_lab_time(self):
        self.lab.edit_lab_time("3-6")
        self.assertEqual(self.lab.lab_time, "3-6")

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

    def setUp(self):
        self.TA = TA('JBravo', 'abc123')
        self.TA.set_full_name('Johnny Bravo')
        self.TA.set_address('2911 N. Oakland Ave. Milwaukee WI 53211')
        self.TA.set_email('JBravo7@uwm.edu')
        self.TA.add_lab_section('Intro to Software Engineering', '414')
        self.TA.add_lab_section('Intro to Artificial Intelligence', '552')
        self.TA.add_grader_course('Intro to Software Engineering')
        self.TA.add_grader_course('Intro to Artificial Intelligence')

    def test_constructor(self):
        username = self.TA.get_username()
        self.assertEqual(username, 'JBravo')
        pw = self.TA.get_password()
        self.assertEqual(pw, 'abc123')

    def test_get_lab_sections(self):
        result = self.TA.get_lab_sections()
        self.assertEqual(result, '[414] Intro to Software Engineering\n[552] Intro to Artificial Intelligence\n')

    def test_add_lab_section(self):
        self.TA.add_lab_section('Intro to Computer Security', '777')
        result = self.TA.get_lab_sections()
        self.assertEqual(result,
                         '[414] Intro to Software Engineering\n[552] Intro to Artificial Intelligence\n[777] Intro to Computer Security\n')

    def test_remove_lab_section(self):
        self.TA.remove_lab_section('Intro to Software Engineering', '414')
        result = self.TA.get_lab_sections()
        self.assertEqual(result, '[552] Intro to Artificial Intelligence\n[777] Intro to Computer Security\n')
        self.TA.remove_lab_section('Intro to Computer Security', '777')
        result = self.TA.get_lab_sections()
        self.assertEqual(result, '[552] Intro to Artificial Intelligence\n')

    def test_get_grader_courses(self):
        result = self.TA.get_grader_courses()
        self.assertEquals(result, 'Intro to Software Engineering, Intro to Artificial Intelligence')

    def test_add_grader_course(self):
        self.TA.add_grader_course('Intro to Computer Security')
        result = self.TA.get_grader_courses()
        self.assertEquals(result,
                          'Intro to Software Engineering, Intro to Artificial Intelligence, Intro to Computer Security')

    def test_remove_grader_course(self):
        self.TA.remove_grader_course('Intro to Artificial Intelligence')
        result = self.TA.get_grader_courses()
        self.assertEquals(result, 'Intro to Software Engineering, Intro to Computer Security')
        self.TA.remove_grader_course('Intro to Computer Security')
        result = self.TA.get_grader_courses()
        self.assertEquals(result, 'Intro to Software Engineering')

    def test_test_view_public_info(self):
        result = self.TA.get_public_contact_info()
        self.assertEquals(result, 'Johnny Bravo\nTA\nJBravo7@uwm.edu')

    def setUp(self):
        self.user = User('wheelerg', '1234')
        self.user.set_full_name('Grant Wheeler')
        self.user.set_address('3200 N. Cramer St. Milwaukee, WI 53211')
        self.user.set_email('wheelerg@uwm.edu')
        self.user.set_phone_number('4148857236')

    def test_constructor(self):
        user = User('patel59', 'iamawesome')
        username = user.username
        password = user.password
        self.assertEqual(username, 'patel59')
        self.assertEqual(password, 'iamawesome')

    def test_get_username(self):
        result = self.user.get_username()
        self.assertEqual(result, 'wheelerg')

    def test_get_password(self):
        result = self.user.get_password()
        self.assertEqual(result, '1234')

    def test_get_full_name(self):
        result = self.user.get_full_name()
        self.assertEquals(result, 'Grant Wheeler')

    def test_get_address(self):
        result = self.user.get_address()
        self.assertEqual(result, '3200 N. Cramer St. Milwaukee, WI 53211')

    def test_get_phone_number(self):
        result = self.user.get_phone_number()
        self.assertEqual(result, '4148857236')

    def test_get_email(self):
        result = self.user.get_email()
        self.assertEqual(result, 'wheelerg@uwm.edu')

    def test_set_username(self):
        self.user.set_username('gwheeler')
        result = self.user.get_username()
        self.assertEquals(result, 'gwheeler')

    def test_set_password(self):
        self.user.set_password('4321')
        result = self.user.get_password()
        self.assertEquals(result, '4321')

    def test_set_full_name(self):
        self.user.set_full_name('Gina Wheeler')
        result = self.user.get_full_name()
        self.assertEquals(result, 'Gina Wheeler')

    def test_set_address(self):
        self.user.set_address('3400 N. Maryland Av. Milwaukee, WI 53211')
        result = self.user.get_address()
        self.assertEquals(result, '3400 N. Maryland Av. Milwaukee, WI 53211')

    def test_set_phone_number(self):
        self.user.set_phone_number('4145882300')
        result = self.user.get_phone_number()
        self.assertEquals(result, '4145882300')

    def test_set_email(self):
        self.user.set_email('gwheeler@uwm.edu')
        result = self.user.get_email()
        self.assertEquals(result, 'gwheeler@uwm.edu')

    def test_parse(self):
        self.assertEqual(None)

    def test_login(self):
        user = User('bkhana', 'hellyeah')
        username = user.username
        password = user.password
        self.assertEqual(username, 'bkhana')
        self.assertEqual(password, 'hellyeah')

    def test_create(self):
        course = Course("Computer", "CS", "Rock", "361")
        coursename = course.course_name
        coursetype = course.course_type
        courseinstructor = course.course_instructor
        coursenumber = course.course_code
        self.assertEqual(coursename, 'Computer')
        self.assertEqual(coursetype, 'CS')
        self.assertEqual(courseinstructor, 'Rock')
        self.assertEqual(coursenumber, '361')

    def test_notify(self):
        self.Supervisor = Supervisor('Harry', '1234')
        self.message = 'Class Cancelled'
        self.notify.Supervisor = (self.message)
        self.assetEquals('Class Cancelled')

    def test_assign(self):
        course = Course("Computer", "CS", "Rock", "361")
        ins = Instructor("bkhanal", "okall")
        ta = TA("bishe", "nepal")
        coursenum = course.course_code
        insname = ins.username
        taname = ta.username
        self.assertEqual(coursenum, '361')
        self.assertEqual(insname, 'bkhanal')
        self.assertEqual(taname, 'bishe')

    def test_logout(self):
        user = User('bkhana', 'hellyeah')
        username = user.username
        password = user.password
        self.assertEqual(None)

    def test_edit(self):
        user = User('bkhana', 'hellyeah')
        username = user.username
        password = user.password
        course = Course("Computer", "CS", "Rock", "361")
        coursename = course.course_name
        coursetype = course.course_type
        courseinstructor = course.course_instructor
        coursenumber = course.course_code
        self.edit.username('bchha')
        self.assertEquals(username, 'bchha')
        self.edit.password('hellno')
        self.assertEquals(password, 'hellno')
        self.edit.coursename('science')
        self.assertEquals(coursename, 'science')
        self.edit.coursetype('SCI')
        self.assertEquals(coursetype, 'SCI')
        self.edit.courseinstructor('Joe')
        self.assertEquals(courseinstructor, 'Joe')
        self.edit.coursenumber('371')
        self.assertEquals(coursenumber, '371')

    def test_access(self):
        self.Supervisor = Supervisor('Harry', '1234')
        self.TA = TA('Ben', '23***abc')
        self.TA.set_full_name('Ben Step')
        self.TA.set_address('2922 N. Kenwood. Milwaukee WI 53211')
        self.TA.set_email('ben7@uwm.edu')
        self.TA.set_PhonNumber('414-883-6231')
        self.TA.add_lab_section('CS351', '701')
        self.TA.add_lab_section('CS251', '552')
        self.TA.add_grader_course('CS351')
        self.TA.add_grader_course('CS251')
        self.access.TA()
        self.assetEquals('Ben Step', '2922 N. Kenwood. Milwaukee WI 53211', 'ben7@uwm.edu' 'CS351', '701')

    def test_delete(self):
        user = User('bkhana', 'hellyeah')
        username = user.username
        password = user.password
        course = Course("Computer", "CS", "Rock", "361")
        coursename = course.course_name
        coursetype = course.course_type
        courseinstructor = course.course_instructor
        coursenumber = course.course_code
        self.delete.courseinstructor('Rock')
        self.assertEquals(course.courseinstructor, None)
        self.delete.course('Computer')
        self.assertEquals(None)

    def test_verify(self):
        ta = TA("bis", "007")
        admin = Administrator("dan", "213")
        sup = Supervisor("jon", "556")
        ins = Instructor("jat", "778")
        com1 = app.set_loggedin(ta.username)
        com2 = app.set_loggedin(sup.username)
        self.assertFalse(com1)
        self.assertTrue(com2)


if __name__ == '__main__':
    unittest.main()
