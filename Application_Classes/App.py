from Application_Classes.CommandController import CommandController


class App(object):
    def __init__(self):
        self.command_controller = CommandController()
        self.set_cmd_controller()
        self.loggedin = None
        pass

    def set_cmd_controller(self):
        self.command_controller.set_pointer_to_app(self)

    def command(self, command, table_data):
        response = self.command_controller.parse(command, table_data)
        return response

    def get_loggedin(self, username):
        return self.command_controller.get_user_by_username(username)

    def get_user(self, username):
        return self.command_controller.get_user_by_username(username)

    def get_course(self, name):
        return self.command_controller.get_course_by_name(name)

    def get_lab(self, number):
        return self.command_controller.get_lab_by_number(number)

    def get_user_object(self, user):
        return self.command_controller.get_user_object(user)

    def get_user_object_byid(self, id):
        return self.command_controller.get_user_object_byid(id)

    def get_course_object(self, course_name):
        return self.command_controller.get_course_object(course_name)

    def get_lab_object(self, lab_number):
        return self.command_controller.get_lab_object(lab_number)

    def set_loggedin(self, new_loggedin):
        self.loggedin = new_loggedin
        pass
