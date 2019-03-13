import unittest
from Skeleton_Classes.Instructor import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor('John', 'Doe')
        self.instructor.set_full_name('Johnny Cage')
        self.instructor.set_address('3208 N. Oakland Ave. Milwaukee WI 53211')
        self.instructor.set_email('JCage7@uwm.edu')
        self.instructor.add_course('Intro to Software Engineering', 'CS', 'Johnny', '414')
        self.instructor.add_course('Intro to Artificial Intelligence ', 'CS', 'Johnny', '289')

    def test_constructor(self):
        username = self.instructor.get_username()
        self.assertEqual(username, 'John')
        pw = self.instructor.get_password()
        self.assertEqual(pw, 'Doe')

    def test_get_courses(self):
        result = self.instructor.get_courses()
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Artificial Intelligence ')

    def test_add_courses(self):
        self.instructor.add_course('Intro to Computer Security', 'CS', 'Johnny', '999')
        result = self.instructor.get_courses()
        self.assertEqual(result,
                         'Intro to Software Engineering\nIntro to Artificial Intelligence\nIntro to Computer Security ')

    def test_remove_course(self):
        course_to_be_removed = 'Intro to Artificial Intelligence'
        self.instructor.remove_course(course_to_be_removed)
        result = self.instructor.get_courses()
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Computer Security ')

    def test_get_public_contact_info(self):
        result = self.instructor.get_public_contact_info()
        self.assertEquals(result, 'Johnny Cage\nInstructor\nJCage7@uwm.edu')


if __name__ == '__main__':
    unittest.main()