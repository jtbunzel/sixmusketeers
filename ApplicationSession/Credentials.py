class Credentials:
    def __init__(self, controller, user = None, DEBUG = False):
        self.controller = controller
        self.user = user
        self.DEBUG = DEBUG
        self.message = ""

    def debug(self, message):
        if self.DEBUG:
            print(message)
            self.message = message