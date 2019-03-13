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



    def test_parse(self):
        self.assertEqual(None )

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
        self.Notification = 'Class Cancelled'e
        self.assertEqual( self.notification, 'Class Cancelled')

    def test_assign(self):

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
        coursenumber = course.course_number
        self.edit.coursename('science')
        self.assertEquals(course.course_name, 'science')
        self.edit.username('bchha')
        self.assertEquals(user.username, 'bchha')


    def test_access(self):

    def test_delete(self):

    def test_assignments(self):

    def test_verify(self):

if __name__ == '__main__':
    unittest.main()

