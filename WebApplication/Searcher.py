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
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(username=queryname).exists():
                return_str = []
                lists = (User.objects.filter(username=queryname).all())
                return_str.append("Username: " + lists.get().username + " ")
                return_str.append("Full name: " + lists.get().name + " ")
                return_str.append("Email: " + lists.get().email + " ")
                return_str.append("Address: " + lists.get().address + " ")
                return_str.append("Phone: " + lists.get().phone + " ")
                return return_str
            else:
                return "username not found"
        elif criteria == "name":
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(name=queryname).exists():
                return_str = []
                lists = (User.objects.filter(name=queryname).all())
                return_str.append("Username: " + lists.get().username + " ")
                return_str.append("Full name: " + lists.get().name + " ")
                return_str.append("Email: " + lists.get().email + " ")
                return_str.append("Address: " + lists.get().address + " ")
                return_str.append("Phone: " + lists.get().phone + " ")
                return return_str
            else:
                return "name not found"
        elif criteria == "role":
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(role=queryname).exists():
                return_str = []
                lists = (User.objects.filter(role=queryname).all())
                return_str.append("Username: " + lists.get().username + " ")
                return_str.append("Full name: " + lists.get().name + " ")
                return_str.append("Email: " + lists.get().email + " ")
                return_str.append("Address: " + lists.get().address + " ")
                return_str.append("Phone: " + lists.get().phone + " ")
                return return_str
            else:
                return "role not found"
        elif criteria == "email":
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(email=queryname).exists():
                return_str = []
                lists = (User.objects.filter(email=queryname).all())
                return_str.append("Username: " + lists.get().username + " ")
                return_str.append("Full name: " + lists.get().name + " ")
                return_str.append("Email: " + lists.get().email + " ")
                return_str.append("Address: " + lists.get().address + " ")
                return_str.append("Phone: " + lists.get().phone + " ")
                return return_str
            else:
                return "email not found"
        elif criteria == "phone":
            for e in User.objects.all():
                print(e.username)
            if User.objects.filter(phone=queryname).exists():
                return_str = []
                lists = (User.objects.filter(phone=queryname).all())
                return_str.append("Username: " + lists.get().username + " ")
                return_str.append("Full name: " + lists.get().name + " ")
                return_str.append("Email: " + lists.get().email + " ")
                return_str.append("Address: " + lists.get().address + " ")
                return_str.append("Phone: " + lists.get().phone + " ")
                return return_str
            else:
                return "phone not found"

    def clean_query(self, queryname):
        strr = []
        lists = (User.objects.filter(username=queryname).all())
        strr.append("Username: " + lists.get().username + " ")
        strr.append("Full name: " + lists.get().name + " ")
        strr.append("Email: " + lists.get().email + " ")
        strr.append("Address: " + lists.get().address + " ")
        strr.append("Phone: " + lists.get().phone + " ")

        print(strr)
        return strr
