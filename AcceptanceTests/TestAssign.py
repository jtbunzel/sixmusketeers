import unittest
from AcceptanceTests import App

class MyTestCase(unittest.TestCase):

    def test_assign_TA_to_course_and_lab_as_supervisor_use_username(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respondToPrompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respondToPrompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respondToPrompt('801')
        self.assertEquals(result, 'wheelerg assigned to CS361 Section 801')

    def test_assign_TA_to_course_and_lab_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respondToPrompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respondToPrompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respondToPrompt('801')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 Section 801')

    def test_assign_TA_to_course_as_grader_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respondToPrompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respondToPrompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respondToPrompt('Grader')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 as Grader')

    def test_assign_TA_to_course_as_supervisor_use_name(self):
        # Assume user logged in is a supervisor
        # Assume course, TA,  and lab section exist

        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respondToPrompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respondToPrompt('CS361')
        self.assertEqual(result, 'Lab Section or Grader?: ')
        result = a.respondToPrompt('N/A')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361')

    def test_assign_TA_to_lab_section_as_instructor_use_name(self):
        # Assume user logged in as instructor
        # Assume TA and lab section exist
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respondToPrompt('Grant Wheeler')
        self.assertEquals(result, 'Course?: ')
        result = a.respondToPrompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respondToPrompt('801')
        self.assertEquals(result, 'Grant Wheeler assigned to CS361 Section 801')

    def test_assign_TA_to_lab_section_as_instructor_use_username(self):
        # Assume user logged in as instructor
        # Assume TA and lab section exist
        # Assume TA assigned to course by supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Name or Username?: ')
        result = a.respondToPrompt('wheelerg')
        self.assertEquals(result, 'Course?: ')
        result = a.respondToPrompt('CS361')
        self.assertEqual(result, 'Lab Section?: ')
        result = a.respondToPrompt('801')
        self.assertEquals(result, 'wheelerg assigned to CS361 Section 801')








if __name__ == '__main__':
    unittest.main()
