from abc import abstractmethod

class User:

    def __init__(self, username, password):
        pass

    def get_username(self):
        pass

    def set_username(self, new_username):
        pass

    def get_password(self):
        pass

    def set_password(self):
        pass

    def get_name(self):
        pass

    def set_full_name(self, new_full_name):
        pass

    def get_full_name(self):
        pass

    def get_phone_number(self):
        pass

    def set_phone_number(self, new_phone_number):
        pass

    def get_address(self):
        pass

    def set_address(self, new_address):
        pass

    def get_email(self):
        pass

    def set_email(self, new_email):
        pass

    @abstractmethod
    def get_public_contact_info(self):
        pass
