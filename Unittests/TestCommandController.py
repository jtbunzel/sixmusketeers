import unittest
from Skeleton_Classes.Administrator import *
from Skeleton_Classes.Course import *
from Skeleton_Classes.User import *
from Skeleton_Classes.App import *
from Skeleton_Classes.Database import *
from Skeleton_Classes.Supervisor import *
# from Skeleton_Classes.Lab_section import *
from Skeleton_Classes.Supervisor import *
# from Skeleton_Classes.TA import *
from Skeleton_Classes.App import *


class TestCommandController(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(None)

    def test_login(self):
        user = User('bkhana', 'hellyeah')
        username = user.username
        password = user.password
        self.assertEqual(username, 'bkhana')
        self.assertEqual(password, 'hellyeah')

    def test_create(self):
        a = App()
        a.set_cmd_controller()
        ## assume this is the way create a user
        user = a.command(
            "create user username_test pass_test firstname_test last_test admin email_test phone_test address_test")
        print(user)
        user1 = user.split(" ") # remove created in confirmation message
        self.assertEqual(user1[1], "username_test")

        a = App()
        a.set_cmd_controller()
        course1 = a.command("create course intro_to_software CS395 Rock 4 tanat")
        course = course1.split(" ")
        self.assertEqual(course[1], "intro_to_software")

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
        self.assertEquals(courseinstructor, None)
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
