from Skeleton_Classes.Database import *
from Skeleton_Classes.App import *


class CommandController(object):

    def __init__(self, app):
        self.database_interface = Database()
        self.app = app

    def parse(self, a):
        self.command= a

    def login(self, username, password):
        if self.app.get_loggedin() is not None:
            return 'User already logged in. Log out to log in as a different user.'
        user_logging_in = self.database_interface.read('username=username')
        if user_logging_in is None:
            return 'User not found.'
        if user_logging_in.password != password:
            return 'Password is incorrect.'
        self.app.set_loggedin(user_logging_in)
        return
    pass

    def create(self, credentials):
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
            model=user()
            model.save(user1)

    def verify(self, commandstr , user):

        if (user.rank ==3 ): # supervisor and administrator
            if (commandstr == "create"):
                self.command(self,a= commandstr).Administrator= "Sorry, not verified"
                self.command(self,a= commandstr).TA = "is verified"
                self.command(self,a= commandstr).Instructor = "verified successfully"
                self.command(self,a= commandstr).Course= "verified successfully"
                self.command(self,a= commandstr).LabSection = "verified successfully"

            if(commandstr== "assign"):
                self.assign.Administrator= "Sorry, not verified"
                self.assign.TA = "verified successfully"
                self.assign.Instructor = "verified successfully"
                self.assign.Course= "verified successfully"
                self.assign.LabSection = "verified successfully"

            if( commandstr == "edit"):
                self.edit.Administrator= "Sorry, not verified"
                self.edit.TA = "is verified"
                self.edit.Instructor = "verified successfully"
                self.edit.Course= "verified successfully"
                self.edit.LabSection = "verified successfully"

            if( commandstr== "delete"):
                self.delete.Administrator= "Sorry, not verified"
                self.delete.TA = "is verified"
                self.delete.Instructor = "verified successfully"
                self.delete.Course= "verified successfully"
                self.delete.LabSection = "verified successfully"

            if (commandstr == "notify"):
                self.notify.Administrator= "Sorry, not verified"
                self.notify.TA = "is verified"
                self.notify.Instructor = "verified successfully"
                self.notify.Course= "verified successfully"
                self.notify.LabSection = "verified successfully"

        if (user.rank ==1 ): # supervisor
            if (commandstr == "create"):
                self.create.Administrator= "is verified"
                self.create.TA = "is verified"
                self.create.Instructor = "verified successfully"
                self.create.Course= "verified successfully"
                self.create.LabSection = "verified successfully"

            if(commandstr== "assign"):
                self.assign.Administrator= "is verified"
                self.assign.TA = "is verified"
                self.assign.Instructor = "verified successfully"
                self.assign.Course= "verified successfully"
                self.assign.LabSection = "verified successfully"

            if( commandstr== "edit"):
                self.edit.Administrator= "is verified"
                self.edit.TA = "is verified"
                self.edit.Instructor = "verified successfully"
                self.edit.Course= "verified successfully"
                self.edit.LabSection = "verified successfully"

            if( commandstr== "delete"):
                self.delete.Administrator= "is verified"
                self.delete.TA = "is verified"
                self.delete.Instructor = "verified successfully"
                self.delete.Course= "verified successfully"
                self.delete.LabSection = "verified successfully"

            if (commandstr == "notify"):
                self.notify.Administrator= "is verified"
                self.delete.TA = "is verified"
                self.delete.Instructor = "verified successfully"
                self.delete.Course= "verified successfully"
                self.delete.LabSection = "verified successfully"

        if (user.rank ==4 ): # TA
            if (commandstr == "create"):
                self.create.Administrator= "not verified"
                self.create.TA = "not verified"
                self.create.Instructor = "not verified "
                self.create.Course= "not verified"
                self.create.LabSection = "not verified"

            if(commandstr== "assign"):
                self.assign.Administrator= "not verified"
                self.assign.TA = "not verified"
                self.assign.Instructor = "not verified "
                self.assign.Course= "not verified"
                self.assign.LabSection = "not verified"


            if( commandstr == "edit"):
                self.edit.Administrator= "not verified"
                self.edit.TA = "not verified"
                self.edit.Instructor = "not verified "
                self.edit.Course= "not verified"
                self.edit.LabSection = "not verified"


            if( commandstr== "delete"):
                self.delete.Administrator= "not verified"
                self.delete.TA = "not verified"
                self.delete.Instructor = "not verified "
                self.delete.Course= "not verified"
                self.delete.LabSection = "not verified"


            if (commandstr == "notify"):
                self.notify.Administrator= "not verified"
                self.notify.TA = "not verified"
                self.notify.Instructor = "not verified "
                self.notify.Course= "not verified"
                self.notify.LabSection = "not verified"

        if (user.rank ==3 ): # Instructor
            if (commandstr == "create"):
                self.create.Administrator= "not verified"
                self.create.TA = "not verified"
                self.create.Instructor = "not verified "
                self.create.Course= "not verified"
                self.create.LabSection = "not verified"

            if(commandstr== "assign"):
                self.assign.Administrator= "not verified"
                self.assign.TA = "not verified"
                self.assign.Instructor = "not verified "
                self.assign.Course= "not verified"
                self.assign.LabSection = "not verified"


            if( commandstr == "edit"):
                self.edit.Administrator= "not verified"
                self.edit.TA = "not verified"
                self.edit.Instructor = "not verified "
                self.edit.Course= "not verified"
                self.edit.LabSection = "not verified"


            if( commandstr == "delete"):
                self.delete.Administrator= "not verified"
                self.delete.TA = "not verified"
                self.delete.Instructor = "not verified "
                self.delete.Course= "not verified"
                self.delete.LabSection = "not verified"


            if (commandstr == "notify"):
                self.notify.Administrator= "not verified"
                self.notify.TA = "not verified"
                self.notify.Instructor = "not verified "
                self.notify.Course= "not verified"
                self.notify.LabSection = "not verified"

    def notify(self, message):
        self.notify.message= message

    def assign(self, username, course):
        pass

    def logout(self, username):
        user_to_be_saved = self.app.get_loggedin()
        self.database_interface.write(user_to_be_saved)
        self.app.set_loggedin(None)
        return 'User logged out.'
        pass

    def edit(self, accountDetails, newDetails):
        pass

    def access(self , dataType):
        pass

    def delete(self, dataType):
        pass

    def assignments(dataType):
        pass
