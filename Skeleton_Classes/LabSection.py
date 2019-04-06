
class LabSection:
    def __init__(self, lab_number="", TA=""):
        self.lab_number = lab_number
        self.TA = TA
        self.course = " "

    def get_lab_number(self):
        return self.lab_number

    def set_lab_number(self, new_lab_number):
        self.lab_number = new_lab_number

    def get_lab_TA(self):
        return self.TA

    def set_lab_TA(self, new_lab_TA):
        self.TA = new_lab_TA

    def get_lab_course(self):
        return self.course

    def set_lab_course(self, new_course):
        self.course = new_course
