from Application_Classes.User import User
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class SuperUserCommandController:
    user = User

    def deleteUser(self, targetUser):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        #        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

        #        #Check if user exists
        #        #if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentUser = User.objects.filter(username=targetUser)
        except ObjectDoesNotExist:
            print("User could not be found.")

        #       #Check if user is attempting to delete its own account
        if self.user.username == currentUser.username:
            return "You can not delete your own account"

        if self.user.username == 'Admin'.casefold():
            return "Can not delete Admin account"

        currentUser.delete()

        return "User successfully deleted."

    #   #Display public info for all users in database.
    def showAll(self):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        #        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

        #        If no entries in database return "Database is Empty"
        databaseCount = User.objects.count()
        if databaseCount < 0:
            return "Database is Empty"

        #        #For each user
        #        #Print all userInfo
        userInfo = ""
        for user in User.objects.all():
            userInfo += user.get_public_contact_info()

        return userInfo

    def create(self, username, user_type):
        if username == "":
            return "input something!"
        user1 = User()
        user1.username = username
        if User.objects.filter(username=user1.username).exists():
            return "user already created"
        if "course" is not user_type:
            user1.role = user_type
            user1.save()
            # username1 = User.objects.filter(username=username)
            # print(username1.username)
            # array = list(User.objects.all())
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(username=user1.username).exists():
                return user1.username, "created"
