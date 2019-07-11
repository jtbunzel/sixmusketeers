from WebApplication.models import User, LabSection
from django.core.exceptions import ObjectDoesNotExist


class LabSectionCommandController:

    # edit the lab with the new information
    def editLabSection(self, lab_number, newLabData):
        try:
            obj = LabSection.objects.get(id=lab_number)
            # make the changes
            for key, value in newLabData.items():
                if value is not "":
                    setattr(obj, key, value)
            obj.save()
        # no lab
        except LabSection.DoesNotExist:
            return 'No Lab Section under this number'

        return "Lab Section information has been successfully updated"

    # remove the lab from the database
    def deleteLabSection(self, lab_number):
        try:
            current_lab = LabSection.objects.get(id=lab_number)
        # no lab
        except LabSection.DoesNotExist:
            return "Failed to delete, Lab Section does not exist!"

        current_lab.delete()

        return "Lab Section has been deleted."
