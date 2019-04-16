import unittest
from Application_Classes.Course import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.c1 = Course("Intro to Software Engineering", "Bob", "CS101")
        self.lab_sections = []
        self.assigned_TA = None
        self.assigned_Grader = None

    def test_setup(self):
        self.assertEqual(self.c1.course_name, "Intro to Software Engineering")
        self.assertEqual(self.c1.course_instructor, "Bob")
        self.assertEqual(self.c1.course_code, "CS101")

    def test_get_course_name(self):
        self.assertEqual(self.c1.get_name(), "Intro to Software Engineering")

    def test_get_course_instructor(self):
        self.assertEqual(self.c1.get_instructor(), "Bob")

    def test_get_course_code(self):
        self.assertEqual(self.c1.course_code, "CS101")

    def test_get_lab_sections(self):
        self.assertEqual(self.c1.get_lab_sections(), [])

    def test_get_assigned_TA(self):
        self.assertEqual(self.c1.get_assigned_TA(), None)

    def test_get_graders(self):
        self.assertEqual(self.c1.get_graders(), None)

    def test_set_name(self):
        self.c1.set_name("Intro to Artificial Intelligence")
        self.assertEqual(self.c1.get_name(), "Intro to Artificial Intelligence")

    def test_set_instructor(self):
        self.c1.set_instructor("John")
        self.assertEqual(self.c1.get_instructor(), "John")

    def test_set_course_code(self):
        self.c1.set_course_code("CS202")
        self.assertEqual(self.c1.get_course_code(), "CS202")

    def test_set_lab_section(self):
        self.c1.set_lab_section("707")
        self.assertEqual(self.c1.get_lab_sections(), ["707"])

    def test_set_assigned_ta(self):
        self.c1.set_assigned_TA("Gary")
        self.assertEqual(self.c1.get_assigned_TA(), "Gary")

    def test_set_grader(self):
        self.c1.set_graders("Harry")
        self.assertEqual(self.c1.get_graders(), "Harry")


if __name__ == '__main__':
    unittest.main()
