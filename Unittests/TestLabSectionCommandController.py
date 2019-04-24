from django.test import TestCase
from Application_Classes.LabSectionCommandController import LabSectionCommandController


class TestLabSectionCommandController(TestCase):
    cmd = LabSectionCommandController()

    def setUp(self):
        pass

    def test_create_lab_section(self):
        cmd = LabSectionCommandController()
        action = cmd.createLabSection("Jojo" , "001", "CS101")
        result = "Successfully created a new Lab Section"
        self.assertEqual(result, action)

    def test_edit_lab_section(self):
        cmd = LabSectionCommandController()
        cmd.createLabSection("Jojo" , "001", "CS101")
        action = cmd.editLabSection("Goku", "002", "CS251")
        result = "Lab Section has been edited."
        self.assertEqual(result, action)

    def test_delete_lab_section(self):
        cmd = LabSectionCommandController()
        cmd.createLabSection("Jojo", "001", "CS101")
        action = cmd.deleteLabSection("001")
        result = "Lab Section has been deleted."
        self.assertEqual(result, action)