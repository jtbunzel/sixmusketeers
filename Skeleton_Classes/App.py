class App(object):

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

        if (user.rank ==3 ): # TA
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

    def set_loggedin(self, username):
        pass