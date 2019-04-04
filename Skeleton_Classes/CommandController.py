class CommandController(object):

    def parse(self, a):
        self.command= a

    def login(self, username, password):
        self.login.username = username
        self.login.password = password

    def create(self, credentials):
        pass

    def notify(self, message):
        self.notify.message= message

    def assign(self, username, course):
        pass

    def logout(self, username):
        pass

    def edit(self, accountDetails, newDetails):
        pass

    def access(self , dataType):
        pass

    def delete(self, dataType):
        pass

    def assignments(dataType):
        pass

    def verify(self, username, a):
        pass