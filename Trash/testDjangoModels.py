from django.test import TestCase
from WebApplication.models import *


class TestDjangoModels(TestCase):
    hunterg = User("007","boyland", "hunterg", "password", "Supervisor", "4142240909", "boyland@uwm.edu", "1234 E. Main St. Milwaukee, WI 53211")
    CS101 = Course("008", "Intro to Comp Sci", "0001", "John Doe")
    SEC007 = LabSection("009", "0x0", "001") #, "Intro Comp Security"


    def setUp(self):
        hunterg = User()
        hunterg.name = "boyland"
        hunterg.username = "hunterg"
        hunterg.password = "password"
        hunterg.role = "Supervisor"
        hunterg.phone = "4142240909"
        hunterg.email = "boyland@uwm.edu"
        hunterg.address = "1234 E. Main St. Milwaukee, WI 53211"

    def test_User_Model(self):
        self.assertEqual(self.hunterg.id, "007")
        self.assertEqual(self.hunterg.name, 'boyland')
        self.assertEqual(self.hunterg.username, 'hunterg')
        self.assertEqual(self.hunterg.password, 'password')
        self.assertEqual(self.hunterg.role, 'Supervisor')
        self.assertEqual(self.hunterg.phone, '4142240909')
        self.assertEqual(self.hunterg.email, 'boyland@uwm.edu')
        self.assertEqual(self.hunterg.address, '1234 E. Main St. Milwaukee, WI 53211')

    def test_Course_Model(self):
        self.assertEqual(self.CS101.id, "008")
        self.assertEqual(self.CS101.course_name, "Intro to Comp Sci")
        self.assertEqual(self.CS101.course_code, "0001")
#        self.assertEqual(self.CS101.course_instructor, "John Doe")

#Does not test properly, For some reason it creates the labsection with the lab_number in the wrong parameter place.
    def test_LabSection_Model(self):
        self.assertEqual(self.SEC007.id, "009")
        self.assertEqual(self.SEC007.lab_tas.name, None)
        self.assertEqual(self.SEC007.lab_number, "0x0")
#        self.assertEqual(self.SEC007.course, "Intro Comp Security")


    def test_course_values(self):
        pass  # CS361 = Course.objects.()


if __name__ == '__main__':
    TestCase.main()
