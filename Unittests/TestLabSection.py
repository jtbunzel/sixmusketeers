import unittest
from Application_Classes.LabSection import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lab = LabSection("801", "Henry", "Intro to Software Engineering")

    def test_setUp(self):
        self.assertEqual(self.lab.lab_number, "801")
        self.assertEqual(self.lab.TA, "Henry")
        self.assertEqual(self.lab.course, "Intro to Software Engineering")

    def test_get_lab_number(self):
        self.assertEqual(self.lab.get_lab_number(), "801")

    def test_get_lab_TA(self):
        self.assertEqual(self.lab.get_lab_TA(), "Henry")

    def test_get_lab_course(self):
        self.assertEqual(self.lab.get_lab_course(), "Intro to Software Engineering")

    def test_setters(self):
        self.lab.set_lab_number("999")
        self.assertEqual(self.lab.get_lab_number(), "999")

    def test_set_TA(self):
        self.lab.set_lab_TA("John")
        self.assertEqual(self.lab.get_lab_TA(), "John")

    def test_set_course(self):
        self.lab.set_lab_course("Intro to Artificial Intelligence")
        self.assertEqual(self.lab.get_lab_course(), "Intro to Artificial Intelligence")


if __name__ == '__main__':
    unittest.main()
