from Skeleton_Classes import Course, Instructor, User
from WebApplication import User


class CommandController(object):

    def parse(self, a):
        pass

    def login(self, username, password):
        pass

    def create(self, type, credentials=""):
        if credentials:
            return Exception
            "enter credentionals"
        credentials_array=credentials.split(" ")
        if "user" == type:
            username=credentials_array[0]
            password=credentials_array[1]
            firstname=credentials_array[2]
            lastname=credentials_array[3]
            role=credentials_array[4]
            email=credentials_array[5]
            phone=credentials_array[6]
            address=credentials_array[7]
            user1=User(username, password, firstname, lastname, role, address, phone, email)
            model = user()
            model.save(user1)
def notify(self, message):
    pass


def assign(self, username, course):
    pass


def logout(self, username):
    pass


def edit(self, accountDetails, newDetails):
    pass


def access(self, dataType):
    pass


def delete(self, dataType):
    pass


def assignments(dataType):
    pass


def verify(self, username, a):
    pass
