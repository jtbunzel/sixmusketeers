import unittest
from Trash.Instructor import *
from Trash.MOCK_course import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor('John', 'Doe')
        self.instructor.set_full_name('Johnny Cage')
        self.instructor.set_address('3208 N. Oakland Ave. Milwaukee WI 53211')
        self.instructor.set_email('JCage7@uwm.edu')
        self.instructor.set_phone_number("414")
        self.instructor.add_course('Intro to Software Engineering')
        self.instructor.add_course('Intro to Artificial Intelligence')
        self.c = Course('Intro to Artificial Intelligence','Rock','361')

    def test_constructor(self):
        username = self.instructor.get_username()
        self.assertEqual(username, 'John')
        pw = self.instructor.get_password()
        self.assertEqual(pw, 'Doe')
        self.instructor.add_course(self.c)#testing with instance from class course
        result = 'Intro to Artificial Intelligence'
        self.assertEqual(result,'Intro to Artificial Intelligence')

    def test_get_courses(self):
        result = self.instructor.get_courses
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Artificial Intelligence\n')

    def test_add_courses(self):
        self.instructor.add_course('Intro to Computer Security')
        result = self.instructor.get_courses
        self.assertEqual(result,
                         'Intro to Software Engineering\nIntro to Artificial Intelligence\nIntro to Computer Security\n')

    def test_remove_course(self):
        course_to_be_removed = 'Intro to Artificial Intelligence'
        self.instructor.remove_course(course_to_be_removed)
        result = self.instructor.get_courses
        self.assertEqual(result, 'Intro to Software Engineering\n')

    def test_get_public_contact_info(self):
        result = self.instructor.get_public_contact_info()
        self.assertEqual(result, 'Johnny Cage\nJCage7@uwm.edu\n414')


if __name__ == '__main__':
    unittest.main()
