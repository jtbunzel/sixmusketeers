import unittest
from Skeleton_Classes.Course import Course, LabSection


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.c1 = Course("Math", "Bob", "MTH101")

    def test_setup(self):
        self.assertEqual(self.c1.course_name, "Math")
        self.assertEqual(self.c1.course_instructor, "Bob")
        self.assertEqual(self.c1.course_code, "MTH101")
        self.c1.set_number_of_lab_sections(4)

    def test_getters(self):
        self.assertEqual(self.c1.get_name(), "Math")
        self.assertEqual(self.c1.get_instructor(), "Bob")
        self.assertEqual(self.c1.course_code, "MTH101")

    def test_set_assigned_TA(self):
        self.c1.set_assigned_TA("tanat")
        tas=[]
        tas = self.c1.get_assigned_TA()
        self.assertEqual(tas[0], "tanat")

    def test_add_lab(self):
        self.c1.add_lab("lab1")
        self.assertEqual(self.c1.lab_name[0], "lab1")


if __name__ == '__main__':
    unittest.main()
