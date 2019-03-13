import unittest
from Skeleton_Classes.Course import Course


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.c1 = Course("Math", "MTH", "Bob", "101")

    def test_setup(self):
        self.assertEqual(self.c1.course_name, "Math")
        self.assertEqual(self.c1.course_type, "MTH")
        self.assertEqual(self.c1.course_instructor, "Bob")
        self.assertEqual(self.c1.course_number, "101")

    def test_getters(self):
        self.assertEqual(self.c1.get_name(), "Math")
        self.assertEqual(self.c1.get_type(), "MTH")
        self.assertEqual(self.c1.get_instructor(), "Bob")
        self.assertEqual(self.c1.get_number(), "101")

    def test_edit_course_instructor(self):
        self.edit_course_instructor("Rock")
        self.assertEqual(self.c1.course_instructor, "Rock")

    def test_add_lab(self):
        self.c1.add_lab("lab1")
        self.assertEqual(self.c1.lab_name[0], "lab1")


if __name__ == '__main__':
    unittest.main()
