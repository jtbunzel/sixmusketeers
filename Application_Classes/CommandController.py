from Application_Classes.User import *
from WebApplication.models import User
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from WebApplication.Searcher import Searcher
from Application_Classes.UserCommandController import UserCommandController
from Application_Classes.CourseCommandController import CourseCommandController


class CommandController(object):

    def set_pointer_to_app(self, app):
        self.app = app
        self.adminsuper_stuff = SuperUserCommandController()
        self.searcher = Searcher()
        self.UserCommandCntrl = UserCommandController()
        self.CourseCommand = CourseCommandController()

    def parse(self, command, table_data):
        if command == 'create':
            creation_type = table_data['data_type']
            return self.adminsuper_stuff.create(creation_type, table_data)
        elif command == 'login':
            username = table_data['username']
            password = table_data['password']
            return self.login(username, password)
        elif command == 'logout':
            return self.logout()
        elif command == 'search':
            print(table_data)
            return self.searcher.searchuser(table_data)
        return

    def get_user_by_username(self, username):
        user_object = User.objects.filter(username__iexact=username)
        if user_object.count() == 0:
            return None
        else:
            return user_object.values()[0]

    def login(self, username, password):
        user_logging_in = User.objects.filter(username__iexact=username)
        if user_logging_in.count() == 0:
            return 'Username not found.'
        if user_logging_in[0].password != password:
            return 'Password is incorrect.'

        return True


