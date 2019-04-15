from .models import User, LabSection
from django.core.exceptions import ObjectDoesNotExist


class LabSectionCommandController:
    user = User

    def createLabSection(self, TA, lab_number, course):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

        #        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

        #        Create NewLabSection
        newLabSection = LabSection()
        newLabSection.lab_tas = TA
        newLabSection.lab_number = lab_number
        newLabSection.course = course

        newLabSection.save()

        return "Successfully created a new Lab Section"


        currentLabSection.save()

        return "Lab Section has been edited."

    def editLabSection(self, TA, lab_number, course):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

#        Check if LabSection exists
#        if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentLabSection = LabSection.objects.filter(lab_number=lab_number)
        except ObjectDoesNotExist:
            print("Lab Section could not be found or does not exist.")

#       #If TA not blank edit TA
        if TA != '':
            currentLabSection.TA = TA

#       #If Lab Number not blank edit Lab Number
        if lab_number != '':
            currentLabSection.lab_number = lab_number

#       #If Course not blank edit Course
        if course != '':
            currentLabSection.course = course

        currentLabSection.save()

        return "Lab Section has been edited."

    def deleteLabSection(self, lab_number):
        # Check for user logged in
        if self.user is None:
            return "You must be logged in"

#        #Check for Supervisor or Admin role
        if self.user.rank < 2:
            return "You do not have permission to use this command"

#        Check if LabSection exists
#        if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist.
        try:
            currentLabSection = LabSection.objects.filter(lab_number=lab_number)
        except ObjectDoesNotExist:
            print("Lab Section could not be found or does not exist.")

        currentLabSection.delete()

        return "Lab Section has been deleted."
