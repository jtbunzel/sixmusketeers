import unittest
from Skeleton_Classes.TA import *


class MyTestCase(unittest.Testcase):
    def setUp(self):
        self.TA = Instructor('JBravo', 'abc123')
        self.TA.set_full_name('Johnny Bravo')
        self.TA.set_address('2911 N. Oakland Ave. Milwaukee WI 53211')
        self.TA.set_email('JBravo7@uwm.edu')
        self.TA.set_phone_number('414-552-7777')
        self.TA.add_course('Intro to Software Engineering', 'CS', 'Johnny', '414')
        self.TA.add_course('Intro to Artificial Intelligence ', 'CS', 'Johnny', '289')

    def test_constructor(self):
        ins = Instructor('Seth', 'Rogen')
        username = ins.get_username()
        self.assertEqual(username, 'Seth')
        pw = ins.get_password()
        self.assertEqual(pw, 'Rogen')

    def test_get_lab_sections(self):

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
