import unittest as bk
from  CommandController import*
from User import *
from Administrator import *
from Course import *
from Instructor import *
from Lab_section import *
from Supervisor import *
from TA import *
from App import *

class TestCommandController(bk.TestCase):
    def setup(self):
        self.command= CommandController(self, Course)
        self.command.User('wheelerg', '1234')
        self.command.set_full_name('Grant Wheeler')
        self.command.set_address('3200 N. Cramer St. Milwaukee, WI 53211')
        self.command.user.set_email('wheelerg@uwm.edu')
        self.command.set_phone_number('4148857236')
        self.command.supervisor = Supervisor('hunterg', 'passwerd')
        self.command.supervisor.set_full_name('Hunter Green')
        self.command.supervisor.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.command.supervisor.set_email('hunterg@uwm.edu')
        self.Command.supervisor.set_phone_number('414-569-8784')
        self.admin = Administrator('hunterg', 'passwerd')
        self.command.admin.set_full_name('Hunter Green')
        self.command.admin.set_address('1107 N. Oregon St. Milwaukee WI 53405')
        self.commanad.admin.set_email('hunterg@uwm.edu')
        self.command.admin.set_phone_number('414-569-8784')


    def test_parse(self):
        pass

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
        coursenumber = course.course_number
        self.assertEqual(coursename, 'Computer')
        self.assertEqual(coursetype, 'CS')
        self.assertEqual(courseinstructor, 'Rock')
        self.assertEqual(coursenumber, '361')


    def test_notify(self):

    def test_assign(self):
        course = Course("Computer", "CS", "Rock", "361")
        instructor = Instrcutor("Rock", "okdone")
        ta = TA("Nat", "okso")
        coursenum = course.course_number
        insname = instructor.username
        taname = ta.username
        self.assertEqual(coursenum, '361')
        self.assertEqual(insname, 'Rock')
        self.assertEqual(taname, 'Nat')

    def test_logout(self):
        none

    def test_edit(self):

    def test_access(self):

    def test_delete(self):

    def test_assignments(self):

    def test_verify(self):

if __name__ == '__main__':
    unittest.main()

