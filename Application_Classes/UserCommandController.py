from WebApplication.models import User
from django.core.exceptions import ObjectDoesNotExist
class UserCommandController:
    user = User()
    def editUser(self,username, newInfo):

        #Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        #Check if user exists
#        #if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentUserInfo = User.objects.filter(username__iexact=username).first()
        except ObjectDoesNotExist:
            print("User could not be found.")

#       #If data_type not blank edit data_type
        if newInfo['data_type'] != '':
            currentUserInfo.data_type = newInfo['data_type']

#       #If username not blank edit username
        if newInfo['username'] != '':
            currentUserInfo.username = newInfo['username']

#       #If name not blank edit name
        if newInfo['name'] != '':
            currentUserInfo.name = newInfo['name']

#       #If Password not blank edit
        if newInfo['password'] != '':
            currentUserInfo.password = newInfo['password']

#       #If user_type not blank edit
        if newInfo['user_type'] != '':
            currentUserInfo.user_type = newInfo['user_type']

#       #If email not blank edit Name
        if newInfo['email'] != '':
            currentUserInfo.email = newInfo['email']

#       #If Phone Number not blank edit Password
        if newInfo['phone'] != '':
            currentUserInfo.phone = newInfo['phone']

#       #If Address not blank edit Address
        if newInfo['address'] != '':
            currentUserInfo.address = newInfo['address']

        currentUserInfo.save()

        return "User information has been successfully updated"

    def showUser(self):
        if self.user is None:
            return "you must be logged in"
        a = "Name = " + self.user.name + "\n"
        b = "Address = " + self.user.address + "\n"
        d = "Phone = " + self.user.phone + "\n"
        e = "Email = " + self.user.email + "\n"

        return a+b+d+e