from Skeleton_Class

class App(object):

    def __init__(self):
        self.command_controller = CommandController()

    def command(self, a):
        if ( a.parse == 'create'):
            self.CommandController.create()

        if (a.parse == 'assign'):
            self.CommandController.assign()

        if (a.parse == 'delete'):
            self.CommandController.delete()

        if (a.parse == 'edit'):
            self.CommandController.edit()

        if (a.parse == 'notify'):
            self.CommandController.notification()


def respond_to_prompt(self, a):
        pass

    def edit(accountDetails, newDetails):
        pass

    def assignments(courses):
        pass

    def access(self):
        pass

    def get_loggedin(self):
        pass

    def set_loggedin(self, user):
        pass