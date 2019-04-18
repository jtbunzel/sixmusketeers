from Application_Classes.User import User
from .models import User
#from Application_Classes.App import App

#app = App()


class Searcher:
    user = User

    def searchuser(self, type, user1):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        if type == "user":
            return \
                #app.command("search", {'data_type': 'user', 'input': user1})


