import unittest
from setup_instructor import app


class MyTestCase(unittest.TestCase):
    def test_login(self):
        a = app()
        result = app.command("login username password")
        self.assetEqual("User logged in", result)
        # assume username is in database with password

    def test_contact_info(self):
        a = app()
        # assume loggen in as instructor
        result = app.command("contact")
        self.assetEqual("User can edit contact information", result)





