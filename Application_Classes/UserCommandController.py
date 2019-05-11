from WebApplication.models import User


class UserCommandController:
    def editUser(self, username, newInfo):
        # user doesn't have a name inputted
        if newInfo['name'] == ' ':
            newInfo['name'] = ""

        # grab user object to edit
        try:
            obj = User.objects.get(username__iexact=username)
            # make changes
            for key, value in newInfo.items():
                if value is not "":
                    setattr(obj, key, value)

            obj.save()

        except User.DoesNotExist:
            return 'No user under this name'

        return "User information has been successfully updated"
