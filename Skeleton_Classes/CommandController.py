from Skeleton_Classes.Database import *
from Skeleton_Classes.App import *
from Skeleton_Classes.User import *
from Skeleton_Classes.Course import *


class CommandController(object):
    def __init__(self):
        self.database_interface = Database()
        self.command = ""

    def parse(self, a):
        self.command = a.split(" ", 1)
        return self.command[0]

    def set_pointer_to_app(self, app):
        self.app = app

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

    def create(self, credentials_array, type):
        if credentials_array == "":
            return Exception
        print(type)
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
            # Database.write(user1)
            return user1  # for testing
        elif "course" == type:
            course = Course()
            print('Enter course name:')
            x = input()
            course.set_name(x)
            print('Enter course code:')
            x = input()
            course.set_course_code(x)
            print('Enter teacher name:')
            x = input()
            course.set_instructor(x)
            print('Enter number of lab sections:')
            x = input()
            course.set_number_of_lab_sections(x)
            #Database.save()
            return course
    def notify(self, message):
        self.notify.message = message

    def assign(self, username, course):
        user_to_assign = self.database_interface.read(username)
        user_to_assign.add_course(course)

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
