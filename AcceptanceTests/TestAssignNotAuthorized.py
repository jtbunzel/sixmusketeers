import unittest
from App import *


class TestAssignNotAuthorized(unittest.TestCase):
    def test_assign__TA_as_TA(self):
        # Assume user logged in as TA
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_instructor_as_TA(self):
        # Assume user logged in as TA
        a = App()
        result = a.command('assign Instructor')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_TA_as_supervisor(self):
        # Assume user logged in as supervisor
        a = App()
        result = a.command('assign Instructor')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_instructor_as_supervisor(self):
        # Assume user logged in as supervisor
        a = App()
        result = a.command('assign TA')
        self.assertEquals(result, 'Command not authorized.')

    def test_assign_instructor_as_instructor(self):
        # Assume user logged in as instructor
        a = App()
        result = a.command('assign Instructor')
        self.assertEquals(result, 'Command not authorized.')


if __name__ == '__main__':
    unittest.main()
