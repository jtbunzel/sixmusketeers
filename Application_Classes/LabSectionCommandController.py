from WebApplication.models import User, LabSection
from django.core.exceptions import ObjectDoesNotExist


class LabSectionCommandController:
    user = User()

    def editLabSection(self, lab_number, newLabData):
        currentLab = LabSection()
        try:
            obj = LabSection.objects.get(lab_number__iexact=lab_number)
            for key, value in newLabData.items():
                if value is not "":
                    setattr(obj, key, value)
            obj.save()
        except LabSection.DoesNotExist:
            return 'No Lab Section under this number'

        return "Lab Section information has been successfully updated"

    def deleteLabSection(self, lab_number):
        currentLab = LabSection()
        try:
            currentLab = LabSection.objects.get(lab_number__iexact=lab_number)
        except LabSection.DoesNotExist:
            return "Failed to delete, Lab Section does not exist!"

        currentLab.delete()

        return "Lab Section has been deleted."
