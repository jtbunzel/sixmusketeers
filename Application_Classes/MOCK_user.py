from abc import abstractmethod


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username

    def get_password(self):
        return self.password

    def get_name(self):
        return self.get_full_name()

    def set_full_name(self, new_full_name):
        self.new_full_name = new_full_name

    def get_full_name(self):
        return self.new_full_name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number=phone_number

    def get_address(self):
        return self.new_address

    def set_address(self, new_address):
        self.new_address = new_address

    def get_email(self):
        return self.new_email

    def set_email(self, new_email):
        self.new_email = new_email
        pass

    @abstractmethod
    def get_public_contact_info(self):
        pass
