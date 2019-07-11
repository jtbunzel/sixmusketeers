class LabSection:
    TA = None
    lab_number = ""
    course = None

    def __init__(self, TA, lab_number, course):
        self.TA = TA
        self.lab_number = lab_number
        self.course = course

    def get_lab_TA(self):
        return self.TA

    def set_lab_TA(self, new_lab_TA):
        self.TA = new_lab_TA

    def get_lab_number(self):
        return self.lab_number

    def set_lab_number(self, new_lab_number):
        self.lab_number = new_lab_number

    def get_lab_course(self):
        return self.course

    def set_lab_course(self, new_course):
        self.course = new_course
