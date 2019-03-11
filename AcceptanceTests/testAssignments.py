# 17A TA will be able to view his course assignments (and not change it) so that he can plan his semester.
import unittest
from App import *

a = App()


class TestAssignments(unittest.TestCase):
    # assume user exists
    # assume user is logged in
    # assume user an instructor or TA
    def test_emptyAssignmentsList(self):
        result = a.command('courses')
        self.assertEqual(result, 'No assignments exist')

    def test_viewAllAssignments(self):
        result = a.command('courses')
        self.assertEqual(result, 'TA: Assignments: ')


if __name__ == '__main__':
    unittest.main()
