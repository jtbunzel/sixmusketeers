from Application_Classes.User import User
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class Searcher:
    user = User

    def searcher(self, user1):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"