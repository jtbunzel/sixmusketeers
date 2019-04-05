from Skeleton_Classes.Database import *
from Skeleton_Classes.App import *
from Skeleton_Classes.User import *


class CommandController(object):

    def __init__(self, app):
        self.database_interface = Database()
        self.app = app

    def parse(self, a):
        self.command = a

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
        if credentials:
            return Exception
            "enter credentionals"
        credentials_array = credentials.split(" ")
        if "user" == type:
            username = credentials_array[0]
            password = credentials_array[1]
            firstname = credentials_array[2]
            lastname = credentials_array[3]
            role = credentials_array[4]
            email = credentials_array[5]
            phone = credentials_array[6]
            address = credentials_array[7]
            user1 = User(username, password, role)
            user1.set_first_name(firstname)
            user1.set_last_name(lastname)
            user1.set_email(email)
            user1.set_phone_number(phone)
            user1.set_address(address)
            model = user()
            model.save(user1)

    def notify(self, message):
        self.notify.message = message

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

    def access(self, dataType):
        pass

    def delete(self, dataType):
        pass

    def assignments(dataType):
        pass

    def verify(self, username, a):
        pass
