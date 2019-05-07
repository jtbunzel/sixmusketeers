from WebApplication.models import User
from django.core.exceptions import ObjectDoesNotExist


class UserCommandController:
    user = User()

    def editUser(self, username, newInfo):

        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        # user doesn't have a name inputted
        if newInfo['name'] == ' ':
            newInfo['name'] = ""

        try:
            obj = User.objects.get(username__iexact=username)
            for key, value in newInfo.items():
                if value is not "":
                    setattr(obj, key, value)

            obj.save()
        except User.DoesNotExist:
            return 'No user under this name'

        return "User information has been successfully updated"

    def showUser(self, username):
        if self.user is None:
            return "you must be logged in"

        try:
            currentUserInfo = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return "User could not be found."

        userInfo = "Username: " + currentUserInfo.username + "Name: " + currentUserInfo.name + "Role: " + currentUserInfo.role + "Phone Number: " + currentUserInfo.phone + "Email: " + currentUserInfo.email + "Address: " + currentUserInfo.address

        return userInfo
