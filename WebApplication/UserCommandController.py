from Skeleton_Classes.User import User
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class UserCommandController:
    user = User

    def editUser(self, userInfo, newInfo):
        #Check for user logged in
        if self.user is None:
            return "You must be logged in"

        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

        #Check if user exists
        #if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentUserInfo = User.objects.get(username = userInfo[0])
        except ObjectDoesNotExist:
            print("User could not be found.")

        if newInfo[0] != None:
            currentUserInfo.username = newInfo[0]

        if newInfo[1] != None:
            currentUserInfo.password = newInfo[1]

        if newInfo[2] != None:
            currentUserInfo.first_name = newInfo[2]

        if newInfo[3] != None:
            currentUserInfo.last_name = newInfo[3]

        if newInfo[4] != None:
            currentUserInfo.phone_number = newInfo[4]

        if newInfo[5] != None:
            currentUserInfo.address = newInfo[5]

        if newInfo[6] != None:
            currentUserInfo.email = newInfo[6]

        if newInfo[7] != None:
            currentUserInfo.rank = newInfo[7]

        currentUserInfo.save()

        return "User information has been successfully updated"




