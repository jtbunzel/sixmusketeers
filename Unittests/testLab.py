import unittest
from Skeleton_Classes.Lab_section import Lab_section


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lab = Lab_section("801", "Henry", "12-3")

    def test_setUp(self):
        self.assertEqual(self.lab.lab_number, "801")
        self.assertEqual(self.lab.TA, "Henry")
        self.assertEqual(self.lab.lab_time, "12-3")

    def test_getters(self):
        self.assertEqual(self.lab.get_info(), "801, Henry, 12-3")

    def test_edit_lab_TA(self):
        self.lab.edit_lab_TA("John")
        self.assertEqual(self.lab.TA, "John")

    def test_edit_lab_time(self):
        self.lab.edit_lab_time("3-6")
        self.assertEqual(self.lab.lab_time, "3-6")


if __name__ == '__main__':
    unittest.main()
