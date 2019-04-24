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


    def showUser(self):
        if self.user is None:
            return "you must be logged in"

        name_table = self.user.name.split(" ")
        first_name = name_table[0]
        last_name = name_table[1]

        a = "First name = " + first_name + "\n"
        b = "Last name = " + last_name + "\n"
        c = "Address = " + self.user.address + "\n"
        d = "Phone = " + self.user.phone + "\n"
        e = "Email = " + self.user.email + "\n"

        return a+b+c+d+e