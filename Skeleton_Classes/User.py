from abc import abstractmethod
from Skeleton_Classes.MOCK_user import *


class User:
    #added field role
    def __init__(self, username, password,firstname,lastname,role,address,phone,email):
        self.username = username
        self.password = password
        self.first_name = firstname
        self.last_name = lastname
        self.address = address
        self.phone_number = phone
        self.email = email

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email

    @abstractmethod
    def get_public_contact_info(self):
        pass
