import unittest
from App import *


class MyTestCase(unittest.TestCase):

    def test_assign_TA_to_lab_section_as_instructor_use_name(self):
        # Assume user logged in as instructor
        # Assume TA and lab section exist
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 Section 801.')

    def test_assign_TA_to_lab_section_as_instructor_use_username(self):
        # Assume user logged in as instructor
        # Assume TA and lab section exist
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'wheelerg assigned to CS361 Section 801.')

    def test_assign_TA_not_assigned_to_course(self):
        # Assume user logged in as instructor
        # Assume TA exists
        # Assume TA NOT assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'TA not assigned to this course.')

    def test_assign_TA_to_nonexistant_lab_section(self):
        # Assume user logged in as instructor
        # Assume TA exists
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respond_to_prompt('847')
        self.assertEquals(result, 'Lab Section does not exist.')


if __name__ == '__main__':
    unittest.main()
