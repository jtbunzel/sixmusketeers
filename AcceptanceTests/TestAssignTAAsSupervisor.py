import unittest
from App import *


class MyTestCase(unittest.TestCase):

    def test_assign_TA_to_course_and_lab_as_supervisor_use_username(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'wheelerg assigned to CS361 Section 801.')

    def test_assign_TA_to_course_and_lab_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('801')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 Section 801.')

    def test_assign_TA_to_course_as_grader_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('Grader')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 as Grader.')

    def test_assign_TA_to_course_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respond_to_prompt('N/A')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361')

    def test_assign_TA_to_nonexistant_course_as_supervisor(self):
        # Assume user logged in as supervisor
        # Assume TA exists
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respond_to_prompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respond_to_prompt('CS575')
        self.assertEqual(result, 'Course does not exist.')

    def test_assign_nonexistant_TA_as_supervisor(self):
        # Assume user logged in as supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or username?: ')
        result = a.respond_to_prompt('Kurt Cobain')
        self.assertEquals(result, 'TA does not exist.')

if __name__ == '__main__':
    unittest.main()
