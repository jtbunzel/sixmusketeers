import unittest


class TestInformation(unittest.TestCase):
    def test_invalidPermission(self):
        a = app()
        result = a.command("information name")
        # the user does not have the correct role
        # must be a TA, instructor, administrator, or a supervisor

        self.assertEqual(result, "user does not have permission")

    def test_invalidName(self):
        a = app()
        result = a.command("information name")
        # user has permission
        # the account does not exist

        self.assertEqual(result, "the data does not exist")

    def test_validEntry(self):
        a = app()
        result = a.command("information name")
        # user has permission
        # the account exists

        self.assertEqual(result, "information returned successfully")