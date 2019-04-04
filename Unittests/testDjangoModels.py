from django.test import TestCase
from WebApplication.models import *


class TestDjangoModels(TestCase):
    def setUp(self):
        Supervisor.object.create(username='boyland',
                                 password='password',
                                 address='1234 E. Main St. Milwaukee, WI 53211',
                                 email='boyland@uwm.edu',
                                 phone_number='4142296986',
                                 full_name='John Boyland')
        Administrator.object.create(username='hunter',
                                    password='password',
                                    address='1235 E. Main St. Milwaukee, WI 53211',
                                    email='hunterg@uwm.edu',
                                    phone_number='4148367276',
                                    full_name='Hunter Green')
        ccheng = Instructor.object.create(username='ccheng',
                                 password='password',
                                 address='1236 E. Main St. Milwaukee, WI 53211',
                                 email='ccheng@uwm.edu',
                                 phone_number='4142295170',
                                 full_name='Christine Cheng')
        rock = Instructor.object.create(username='rock',
                                 password='password',
                                 address='1237 E. Main St. Milwaukee, WI 53211',
                                 email='rock@uwm.edu',
                                 phone_number='4142294994',
                                 full_name='Jayson Rock')
        tanawat = TA.object.create(username='tanawat',
                                   password='password',
                                   address='1238 E. Main St. Milwaukee, WI 53211',
                                   email='tanawat@uwm.edu',
                                   phone_number='4142294994',
                                   full_name='Tanawat Kuhnlerkit')
        prasada = TA.object.create(username='prasada',
                                   password='password',
                                   address='1239 E. Main St. Milwaukee, WI 53211',
                                   email='prasada@uwm.edu',
                                   phone_number='4142294994',
                                   full_name='Apoorv Prasad')
        CS395 = Course.create(course_code='CS395',
                              course_name='Social, Professional, and Ethical Issues',
                              course_instructor=ccheng,
                              course_TA_grader=prasada)
        CS361 = Course.create(course_code='CS361',
                              course_name='Introduction to Software Engineering',
                              course_instructor=rock)
        CS361.add.courseTAs(tanawat)
        CS361.add.courseTAs(prasada)
        LabSection.object.create(section_number=801,
                                 course=CS361,
                                 section_TA=tanawat)
        LabSection.object.create(section_number=802,
                                 course=CS361,
                                 section_TA=tanawat)
        LabSection.object.create(section_number=803,
                                 course=CS361,
                                 section_TA=prasada)

    def test_Administrator_values(self):
        boyland = Administrator.objects.all()
        self.assertEqual(boyland.username, 'boyland')
        self.assertEqual(boyland.password, 'password')
        self.assertEqual(boyland.address, '1234 E. Main St. Milwaukee, WI 53211')
        self.assertEqual(boyland.email, 'boyland@uwm.edu')
        self.assertEqual(boyland.phone_number, '4142296986')
        self.assertEqual(boyland.full_name, 'John Boyland')

    def test_Supervisor_values(self):
        hunterg = Supervisor.objects.all()
        self.assertEqual(hunterg.username, 'hunterg')
        self.assertEqual(hunterg.password, 'password')
        self.assertEqual(hunterg.address, '1235 E. Main St. Milwaukee, WI 53211')
        self.assertEqual(hunterg.email, 'hunterg@uwm.edu')
        self.assertEqual(hunterg.phone_number, '4148367276')
        self.assertEqual(hunterg.full_name, 'Hunter Green')

    def test_Instructor_values(self):
        ccheng = Instructor.objects.all().filter(full_name='Christine Cheng')
        self.assertEqual(ccheng.username, 'ccheng')
        self.assertEqual(ccheng.password, 'password')
        self.assertEqual(ccheng.address, '1236 E. Main St. Milwaukee, WI 53211')
        self.assertEqual(ccheng.email, 'ccheng@uwm.edu')
        self.assertEqual(ccheng.phone_number, '4142295170')
        self.assertEqual(ccheng.full_name, 'Chirstine Cheng')

    def test_course_values(self):
        pass  # CS361 = Course.objects.()


if __name__ == '__main__':
    TestCase.main()
