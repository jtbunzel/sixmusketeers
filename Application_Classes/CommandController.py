from Application_Classes.User import *
from Application_Classes.Course import *
from WebApplication.models import User
from WebApplication.AdminSuperCommandController import SuperUserCommandController
from WebApplication.Searcher import Searcher
from WebApplication.UserCommandController import UserCommandController


class CommandController(object):

    def set_pointer_to_app(self, app):
        self.app = app
        self.adminsuper_stuff = SuperUserCommandController()
        self.searcher = Searcher
        self.UserCommandCntrl = UserCommandController()

    def parse(self, command_string):
        command_array = command_string.split(" ")
        command = command_array[0]
        if command == 'create':
            creationtype = command_array[1]
            return self.adminsuper_stuff.create(command_array[2:], creationtype)
        if command == 'login':
            username = command_array[1]
            password = command_array[2]
            return self.login(username, password)
        if command == 'logout':
            return self.logout()
        return

    def get_logged_in(self, username):
        user_object = User.objects.filter(username=username)
        if user_object.count() == 0:
            return None
        else:
            return user_object.values()[0]

    def login(self, username, password):
        user_logging_in = User.objects.filter(username=username)
        if user_logging_in.count() == 0:
            return 'Username not found.'
        if user_logging_in[0].password != password:
            return 'Password is incorrect.'

        return True

    def createUser(self, username):
        num_users_with_same_username = User.objects.filter(username=username).count()
        if num_users_with_same_username != 0:
            return False
        User.objects.create(username=username)
        return True

    def notify(self, message):
        self.notify.message = message

    def assign(self, username, course):
        user_to_assign = self.database_interface.read(username)
        user_to_assign.add_course(course)

    def logout(self):
        self.app.set_loggedin(None)
        return 'User logged out.'

    def edit(self, accountDetails, newDetails):
        pass

    def access(self, dataType):
        pass

    def delete(self, dataType):
        pass

    def assignments(dataType):
        pass

    def verify(self, user, a):
        if (user.rank < 3):

            if self.parse(a) == 'create_TA':
                return True
            if (self.parse(a) == 'create instructor'):
                return True
            if (self.parse(a) == 'create_course'):
                return True
            if (self.parse(a) == 'create_labSection'):
                return True
            if (self.parse(a) == 'create_supervisor'):
                return False

            if (self.parse(a) == 'notify_admin'):
                return True
            if (self.parse(a) == 'notify_TA'):
                return True
            if (self.parse(a) == 'notify_instructor'):
                return True

            if (self.parse(a) == 'assign_TA_labSection'):
                return True
            if (self.parse(a) == 'assign_instructor_cousre'):
                return True
            if (self.parse(a) == 'assign_Adminsistrator'):
                return False
            if (self.parse(a) == 'assign_supervisor'):
                return False

            if (self.parse(a) == 'edit_TA'):
                return True
            if (self.parse(a) == 'edit_instructor'):
                return True
            if (self.parse(a) == 'edit_course'):
                return True
            if (self.parse(a) == 'edit_labSection'):
                return True

            if (self.parse(a) == 'remove_TA'):
                return True
            if (self.parse(a) == 'remove_instructor'):
                return True
            if (self.parse(a) == 'remove_course'):
                return True
            if (self.parse(a) == 'remove_labSection'):
                return True
            if (self.parse(a) == 'remove_supervisor'):
                return False

            if (self.parse(a) == 'access_Ta'):
                return True
            if (self.parse(a) == 'access_instructor'):
                return True
            if (self.parse(a) == 'access_course'):
                return True
            if (self.parse(a) == 'access_labSection'):
                return True

        if (user.rank < 2):
            if (self.parse(a) == 'create_administrator'):
                return True
            if (self.parse(a) == 'notify_administrator'):
                return True
            if (self.parse(a) == 'access_administrator'):
                return True
            if (self.parse(a) == 'edit_administrator'):
                return True

        if (user.rank == 3):
            if (self.parse(a) == 'create_TA'):
                return False
            if (self.parse(a) == 'create_instructor'):
                return False
            if (self.parse(a) == 'create_course'):
                return False
            if (self.parse(a) == 'create_labSection'):
                return False
            if (self.parse(a) == 'create_Adminsistrator'):
                return False
            if (self.parse(a) == 'create_supervisor'):
                return False

            if (self.parse(a) == 'notify_TA'):
                return True
            if (self.parse(a) == 'notify_instructor'):
                return False
            if (self.parse(a) == 'notify_Adminsistrator'):
                return False
            if (self.parse(a) == 'notify_supervisor'):
                return False

            if (self.parse(a) == 'assign_TA_labSection'):
                return True
            if (self.parse(a) == 'assign_instructor_cousre'):
                return True
            if (self.parse(a) == 'assign_Adminsistrator'):
                return False
            if (self.parse(a) == 'assign_supervisor'):
                return False

            if (self.parse(a) == 'edit_TA'):
                return True
            if (self.parse(a) == 'edit_instructor'):
                return False
            if (self.parse(a) == 'edit_course'):
                return True
            if (self.parse(a) == 'edit_labSection'):
                return True
            if (self.parse(a) == 'edit_Adminsistrator'):
                return False
            if (self.parse(a) == 'edit_supervisor'):
                return False

            if (self.parse(a) == 'remove_TA'):
                return False
            if (self.parse(a) == 'remove_instructor'):
                return False
            if (self.parse(a) == 'remove_course'):
                return False
            if (self.parse(a) == 'remove_labSection'):
                return False
            if (self.parse(a) == 'remove_Adminsistrator'):
                return False
            if (self.parse(a) == 'remove_supervisor'):
                return False

            if (self.parse(a) == 'access_Ta'):
                return True
            if (self.parse(a) == 'access_instructor'):
                return False
            if (self.parse(a) == 'access_course'):
                return True
            if (self.parse(a) == 'access_labSection'):
                return True
            if (self.parse(a) == 'access_Adminsistrator'):
                return False
            if (self.parse(a) == 'access_supervisor'):
                return False

        if (user.rank == 4):
            if (self.parse(a) == 'create_TA'):
                return False
            if (self.parse(a) == 'create_instructor'):
                return False
            if (self.parse(a) == 'create_course'):
                return False
            if (self.parse(a) == 'create_labSection'):
                return False
            if (self.parse(a) == 'create_Adminsistrator'):
                return False
            if (self.parse(a) == 'create_supervisor'):
                return False

            if (self.parse(a) == 'notify_TA'):
                return False
            if (self.parse(a) == 'notify_instructor'):
                return False
            if (self.parse(a) == 'notify_Adminsistrator'):
                return False
            if (self.parse(a) == 'notify_supervisor'):
                return False

            if (self.parse(a) == 'assign_TA_labSection'):
                return False
            if (self.parse(a) == 'assign_instructor_cousre'):
                return False
            if (self.parse(a) == 'assign_Adminsistrator'):
                return False
            if (self.parse(a) == 'assign_supervisor'):
                return False

            if (self.parse(a) == 'edit_TA'):
                return False
            if (self.parse(a) == 'edit_instructor'):
                return False
            if (self.parse(a) == 'edit_course'):
                return False
            if (self.parse(a) == 'edit_labSection'):
                return False
            if (self.parse(a) == 'edit_Adminsistrator'):
                return False
            if (self.parse(a) == 'edit_supervisor'):
                return False

            if (self.parse(a) == 'remove_TA'):
                return False
            if (self.parse(a) == 'remove_instructor'):
                return False
            if (self.parse(a) == 'remove_course'):
                return False
            if (self.parse(a) == 'remove_labSection'):
                return False
            if (self.parse(a) == 'remove_Adminsistrator'):
                return False
            if (self.parse(a) == 'remove_supervisor'):
                return False

            if (self.parse(a) == 'access_Ta'):
                return False
            if (self.parse(a) == 'access_instructor'):
                return False
            if (self.parse(a) == 'access_course'):
                return False
            if (self.parse(a) == 'access_labSection'):
                return False
            if (self.parse(a) == 'access_Adminsistrator'):
                return False
            if (self.parse(a) == 'access_supervisor'):
                return False
