from .models import User


class Searcher:
    user = User

    def searchuser(self, table_data):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"
        criteria = table_data['criteria']
        queryname = table_data['string']
        if criteria == "username":
            # list =  list(User.objects.all())
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(username=queryname).exists():
                return self.clean_query(queryname)
            else:
                return "username not found"
        if criteria == "name":
            # list =  list(User.objects.all())
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(name=queryname).exists():
                return self.clean_query(queryname)
            else:
                return "username not found"
        if criteria == "role":
            # list =  list(User.objects.all())
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(role=queryname).exists():
                return self.clean_query(queryname)
            else:
                return "username not found"
        if criteria == "email":
            # list =  list(User.objects.all())
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(email=queryname).exists():
                return self.clean_query(queryname)
            else:
                return "username not found"
        if criteria == "phone":
            # list =  list(User.objects.all())
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(phone=queryname).exists():
                return self.clean_query(queryname)
            else:
                return "username not found"

    def clean_query(self, queryname):
        strr = []
        lists = (User.objects.filter(username=queryname).all())
        # strr = strr + "Username: " + lists.get().username + " "
        # strr = strr + "Full name: " + lists.get().name + " "
        # strr = strr + "Role: " + lists.get().role + " "
        # strr = strr + "Email: " + lists.get().email + " "
        # strr = strr + "Address: " + lists.get().address + " "
        # strr = strr + "Phone: " + lists.get().phone + " "
        strr.append("Username: " + lists.get().username + " ")
        strr.append("Full name: " + lists.get().name + " ")
        strr.append("Email: " + lists.get().email + " ")
        strr.append("Address: " + lists.get().address + " ")
        strr.append("Phone: " + lists.get().phone + " ")

        print(strr)
        return strr
