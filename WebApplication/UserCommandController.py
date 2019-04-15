from Application_Classes.User import User
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class UserCommandController:
    user = User

    def editUser(self, userInfo, newInfo):
        #Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

#        #Check if user exists
#        #if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentUserInfo = User.objects.filter(username__iexact=userInfo[0])
        except ObjectDoesNotExist:
            print("User could not be found.")

#       #If Username not blank edit Username
        if newInfo[0] != '':
            currentUserInfo.username = newInfo[0]

#       #If Password not blank edit Password
        if newInfo[1] != '':
            currentUserInfo.password = newInfo[1]

#       #If First Name not blank edit First Name
        if newInfo[2] != '':
            currentUserInfo.name = newInfo[2]

#       #If Last Name not blank edit Last Name
        if newInfo[3] != '':
            currentUserInfo.last_name = newInfo[3]

#       #If Phone Number not blank edit Phone Number
        if newInfo[4] != '':
            currentUserInfo.phone_number = newInfo[4]

#       #If Address not blank edit Address
        if newInfo[5] != '':
            currentUserInfo.address = newInfo[5]

#       #If Email not blank edit Email
        if newInfo[6] != '':
            currentUserInfo.email = newInfo[6]

#       #If Rank not blank edit Rank
        if newInfo[7] != '':
            currentUserInfo.rank = newInfo[7]

        currentUserInfo.save()

        return "User information has been successfully updated"

    def showUser(self):
        if self.user is None:
            return "you must be logged in"

        a = "First name = " + self.user.first_name + " "
        b = "Last name = " + self.user.last_name + " "
        c = "Address = " + self.user.address + " "
        d = "Phone = " + self.user.phone + " "
        e = "Email = " + self.user.email + " "

        return a+b+c+d+e

    




