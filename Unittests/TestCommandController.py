import unittest as bk
from  Skeleton_Classes.CommandController import*
from  Skeleton_Classes.Administrator import*
from  Skeleton_Classes.Course import*
from  Skeleton_Classes.User import*
from  Skeleton_Classes.App import*
from  Skeleton_Classes.Database import*
from  Skeleton_Classes.Supervisor import*
from  Skeleton_Classes.Lab_section import*
from  Skeleton_Classes.Supervisor import*
from  Skeleton_Classes.TA import*

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
        self.Notification = 'Class Cancelled'
        self.assertEqual( self.notification, 'Class Cancelled')

    def test_assign(self):

    def test_logout(self):


    def test_edit(self):

    def test_access(self):

    def test_delete(self):

    def test_assignments(self):

    def test_verify(self):

if __name__ == '__main__':
    unittest.main()

