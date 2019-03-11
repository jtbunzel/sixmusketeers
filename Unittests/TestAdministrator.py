import unittest
from App import *

a = App()


class testAdministrator(unittest.Testcase):

    def setup(self):

    def tearDown(self):
        pass

    def test_AdministratorLogin(self):
        #assume username is in the database with password
        a= app();
        result= a.command("login username password")
        self.asserEqual("username logged in", result)

    def test_createCourses(self):
        # admin can create course
        # course will appears under schedule catalog
        a = app();
        result = a.command("login username password")
        self.asserEqual("username logged in", result)

    def test_createInstructorAccount(self):
        a = app();
        result = a.command("login username password")
        self.asserEqual("username logged in", result)
#The TA will receive an email notification that their account is now active.#
    def test_createTAAccount(self):
        a = app();
        result = a.command("login username password")
        self.asserEqual("username logged in", result)

    def test_DelectInstructorAccount(self):
        #Admin can delect instructor account for those who doesn't hold the Instructor poistions
        #
        a = app();
        result = a.command("delete instructor account")
        self.asserEqual("username logged in", result)


    def test_DelectTaAccount(self):
        a = app();
        result = a.command("login username password")
        self.asserEqual("username logged in", result)

    def test_EditAccount(self):
        a = app();
        result = a.command("login username password")
        self.asserEqual("username logged in", result)

    def test_SendNotification(self):
        a = app();
        result = a.command("login username password")
        self.asserEqual("username logged in", result)

    def test_AccessDataOnSystem(self):
    # admin can access all data on system
        a= app();
        result= a.command("can access all data in system")
        self.asserEqual("username logged in", result)



 if __name__ == '__main__':
    unittest.main()