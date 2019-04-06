from Skeleton_Class

class App(object):

    def __init__(self):
        self.command_controller = CommandController()

    def command(self, a):
        if ( a.parse == 'create'):
            self.create

        if (a.parse == 'assign'):
            self.assign

        if (a.parse == 'delete'):
            self.delete

        if (a.parse == 'edit'):
            self.edit

        if (a.parse == 'notify'):
            self.notiy


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