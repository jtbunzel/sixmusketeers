from WebApplication.models import User, Course, LabSection
from Application_Classes.AdminSuperCommandController import SuperUserCommandController
from Application_Classes.Searcher import Searcher
from Application_Classes.UserCommandController import UserCommandController
from Application_Classes.CourseCommandController import CourseCommandController
from Application_Classes.LabSectionCommandController import LabSectionCommandController


class CommandController(object):

    def set_pointer_to_app(self, app):
        self.app = app
        self.adminsuper_stuff = SuperUserCommandController()
        self.searcher = Searcher()
        self.UserCommandCntrl = UserCommandController()
        self.CourseCommand = CourseCommandController()
        self.LabCommand = LabSectionCommandController()

    # takes the command and variables and runs the correct function
    def parse(self, command, table_data):
        if command == 'create':
            creation_type = table_data['data_type']
            return self.adminsuper_stuff.create(creation_type, table_data)
        elif command == 'login':
            username = table_data['username']
            password = table_data['password']
            return self.login(username, password)
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
            lab_number = table_data['lab_id']
            return self.LabCommand.editLabSection(lab_number, table_data)
        elif command == 'deleteCourse':
            course_name = table_data['course_name']
            return self.CourseCommand.deleteCourse(course_name)
        elif command == 'deleteLab':
            lab_number = table_data['lab_id']
            return self.LabCommand.deleteLabSection(lab_number)

    # returns the user as a list by username
    def get_user_by_username(self, username):
        user_object = User.objects.filter(username__iexact=username)
        if user_object.count() == 0:
            return None
        else:
            return user_object.values()[0]

    # returns the course as a list by name
    def get_course_by_name(self, name):
        course_object = Course.objects.filter(course_name__iexact=name)
        if course_object.count() == 0:
            return None
        else:
            return course_object.values()[0]

    # returns the lab as a list by id
    def get_lab(self, number):
        lab_object = LabSection.objects.filter(id=number)
        if lab_object.count() == 0:
            return None
        else:
            return lab_object.values()[0]

    # return the user object by username
    def get_user_object(self, username):
        if username == "None":
            return None

        user_object = User.objects.get(username__iexact=username)
        return user_object

    # returns the user object by id
    def get_user_object_byid(self, id):
        if id is None:
            return None

        user_object = User.objects.get(id=id)
        return user_object

    # returns the course object by name
    def get_course_object(self, course_name):
        if course_name == "None":
            return None

        course_object = Course.objects.get(course_name=course_name)
        return course_object

    # returns the lab object by id
    def get_lab_object(self, lab_number):
        if lab_number == "None":
            return None

        lab_object = LabSection.objects.get(id=lab_number)
        return lab_object

    # performs the login and verifies the username and password
    def login(self, username, password):
        # try to grab user
        try:
            user_logging_in = User.objects.get(username__iexact=username)

            if user_logging_in.password == password:
                # everything looks good!
                response = "Correct login"
            else:
                # password is incorrect
                response = "Incorrect password."

        except User.DoesNotExist:
            # user does not exist
            response = "Username does not exist."

        return response

    # grabs an overall count of all the objects for the homepage
    def get_database_count(self):
        objects = {
            'num_users': User.objects.all().count(),
            'num_courses': Course.objects.all().count(),
            'num_labs': LabSection.objects.all().count()
        }

        return objects




