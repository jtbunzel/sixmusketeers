from Trash.LabSection import LabSection
from django.test import TestCase

class TestLabSection(TestCase):

    def test_get_lab_ta(self):
        lab = LabSection("John", 801, "Introduction to Artificial Intelligence")
        self.assertEqual(lab.TA, "John")