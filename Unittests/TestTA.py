import unittest
from Application_Classes.TA import *


class MyTestCase(unittest.TestCase):
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
        self.assertEqual(result, '[552] Intro to Artificial Intelligence\n[777] Intro to Computer Security')
        self.TA.remove_lab_section('Intro to Computer Security', '777')
        result = self.TA.get_lab_sections()
        self.assertEqual(result, '[552] Intro to Artificial Intelligence\n')

    def test_get_grader_courses(self):
        result = self.TA.get_grader_courses()
        self.assertEqual(result, 'Intro to Software Engineering\nIntro to Artificial Intelligence\n')

    def test_add_grader_course(self):
        self.TA.add_grader_course('Intro to Computer Security')
        result = self.TA.get_grader_courses()
        self.assertEqual(result,
                          'Intro to Software Engineering\nIntro to Artificial Intelligence\nIntro to Computer Security\n')

    def test_remove_grader_course(self):
        self.TA.remove_grader_course('Intro to Artificial Intelligence')
        result = self.TA.get_grader_courses()
        self.assertEqual(result, 'Intro to Software Engineering\n')
        self.TA.remove_grader_course('Intro to Software Engineering')
        result = self.TA.get_grader_courses()
        self.assertEqual(result, '')

    def test_view_public_info(self):
        result = self.TA.get_public_contact_info()
        self.assertEquals(result, 'Johnny Bravo\nTA\nJBravo7@uwm.edu')


if __name__ == '__main__':
    unittest.main()
