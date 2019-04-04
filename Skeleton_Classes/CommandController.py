from Skeleton_Classes.Database import *
from Skeleton_Classes.App import *


class CommandController(object):

    def __init__(self, app):
        self.database_interface = Database()
        self.app = app

    def parse(self, a):
        self.command= a

    def login(self, username, password):
        if self.app.get_loggedin() is not None:
            return 'User already logged in. Log out to log in as a different user.'
        user_logging_in = self.database_interface.read('username=username')
        if user_logging_in is None:
            return 'User not found.'
        if user_logging_in.password != password:
            return 'Password is incorrect.'
        self.app.set_loggedin(user_logging_in)
        return
    pass

    def create(self, credentials):
        pass

    def notify(self, message):
        self.notify.message= message

    def assign(self, username, course):
        pass

    def logout(self, username):
        user_to_be_saved = self.app.get_loggedin()
        self.database_interface.write(user_to_be_saved)
        self.app.set_loggedin(None)
        return 'User logged out.'
        pass

    def edit(self, accountDetails, newDetails):
        pass

    def access(self , dataType):
        pass

    def delete(self, dataType):
        pass

    def assignments(dataType):
        pass

    def verify(self, username, a):
        pass