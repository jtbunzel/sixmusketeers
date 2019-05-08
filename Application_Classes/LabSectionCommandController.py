from WebApplication.models import User, LabSection
from django.core.exceptions import ObjectDoesNotExist


class LabSectionCommandController:
    user = User()

    def editLabSection(self, lab_number, newLabData):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"
        try:
            obj = LabSection.objects.get(id=lab_number)
            for key, value in newLabData.items():
                if value is not "":
                    setattr(obj, key, value)
            obj.save()
        except LabSection.DoesNotExist:
            return 'No Lab Section under this number'

        return "Lab Section information has been successfully updated"

    def deleteLabSection(self, lab_number):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"
        try:
            currentLab = LabSection.objects.get(id=lab_number)
        except LabSection.DoesNotExist:
            return "Failed to delete, Lab Section does not exist!"

        currentLab.delete()

        return "Lab Section has been deleted."
