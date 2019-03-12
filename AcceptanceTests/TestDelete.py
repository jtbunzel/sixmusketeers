import unittest


class TestDelete(unittest.TestCase):
    def test_invalidPermission(self):
        a = app()
        result = a.command("delete dataType name")
        # the user does not have the correct role

        self.assertEqual(result, "user does not have permission")

    def test_invalidDataType(self):
        a = app()
        result = a.command("delete dataType name")
        # the data type is not valid

        self.assertEqual(result, "the datatype is not class or acocunt")

    def test_invalidName(self):
        a = app()
        result = a.command("delete dataType name")
        # the data does not exist

        self.assertEqual(result, "the data does not exist")

    def test_validDataType_InvalidName(self):
        a = app()
        result = a.command("delete dataType name")
        # the datatype is valid but the data does not exist

        self.assertEqual(result, "there is no data under this name")

    def test_validEntry(self):
        a = app()
        result = a.command("delete dataType name")
        # the datatype is either class or account
        # the data exists

        self.assertEqual(result, "data deleted suggessfully")