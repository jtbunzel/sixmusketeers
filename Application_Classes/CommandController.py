from WebApplication.models import User, Course
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from Application_Classes.Searcher import Searcher
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
            return self.searcher.searchuser(table_data)
        elif command == 'searchCourse':
            return self.searcher.searchCourse(table_data)
        elif command == 'searchLab':
            return self.searcher.searchLabSection(table_data)
        elif command == 'editUser':
            username = table_data['username']
            return self.UserCommandCntrl.editUser(username, table_data)
        elif command == 'deleteAccount':
            username = table_data['username']
            return self.adminsuper_stuff.deleteUser(username)
        elif command == 'editCourse':
            course_name = table_data['course_name']
            return self.CourseCommand.editCourse(course_name, table_data)
        elif command == 'editLab':
            lab_number = table_data['lab_number']
            return self.CourseCommand.editCourse(lab_number, table_data)
        elif command == 'deleteCourse':
            course_name = table_data['course_name']
            return self.CourseCommand.deleteCourse(course_name)
        elif command == 'deleteLab':
            lab_number = table_data['lab_number']
            return self.CourseCommand.deleteCourse(lab_number)

    def get_user_by_username(self, username):
        user_object = User.objects.filter(username__iexact=username)
        if user_object.count() == 0:
            return None
        else:
            return user_object.values()[0]

    def get_course_by_name(self, name):
        course_object = Course.objects.filter(course_name__iexact=name)
        if course_object.count() == 0:
            return None
        else:
            return course_object.values()[0]

    def get_lab_by_number(self, number):
        lab_object = Course.objects.filter(lab_number__iexact=number)
        if lab_object.count() == 0:
            return None
        else:
            return lab_object.values()[0]

    def get_user_object(self, username):
        print("object: " + username)
        if username == "None":
            return None

        user_object = User.objects.get(username__iexact=username)
        return user_object

    def get_user_object_byid(self, id):
        print("object: " + id)
        if id is None:
            return None

        user_object = User.objects.get(id=id)
        return user_object

    def get_course_object(self, course_name):
        if course_name == "None":
            return None

        course_object = Course.objects.get(course_name=course_name)
        return course_object

    def get_lab_object(self, lab_number):
        if lab_number == "None":
            return None

        lab_object = Course.objects.get(lab_number=lab_number)
        return lab_object

    def login(self, username, password):
        user_logging_in = User.objects.filter(username__iexact=username)
        if user_logging_in.count() == 0:
            return 'Username not found.'
        if user_logging_in[0].password != password:
            return 'Password is incorrect.'

        return True


