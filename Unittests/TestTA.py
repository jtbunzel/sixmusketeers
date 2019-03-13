import unittest
from Skeleton_Classes.TA import *


class MyTestCase(unittest.Testcase):
    def setUp(self):
        self.TA = TA('JBravo', 'abc123')
        self.TA.set_full_name('Johnny Bravo')
        self.TA.set_address('2911 N. Oakland Ave. Milwaukee WI 53211')
        self.TA.set_email('JBravo7@uwm.edu')
        self.TA.set_phone_number('414-552-7777')
        self.TA.add_lab_section("414", "Johnny", "10-12")
        self.TA.add_lab_section("552", "Johnny", "2-4")

    def test_constructor(self):
        username = self.TA.get_username()
        self.assertEqual(username, 'JBravo')
        pw = self.TA.get_password()
        self.assertEqual(pw, 'abc123')

    def test_get_lab_sections(self):
        result = self.Ta.get_lab_sections()
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Artificial Intelligence ')

    def test_add_lab_section(self, course, section):
        pass

    def test_remove_lab_section(self, course, section):
        pass

    def test_get_grader_courses(self):
        pass

    def test_add_grader_course(self, course):
        pass

    def test_remove_grader_course(self, course):
        pass

    def test_test_view_public_info(self):
        result = a.access(self)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
