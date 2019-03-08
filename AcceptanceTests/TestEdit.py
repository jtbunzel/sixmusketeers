import unittest as bk

class TestEdit(bk):
    a = app()
        # assume user exists
        # assume user is logged in
        # assume user is supervisor
        #assume user is administor
        # assume user is instructors and TAs

    def test_supervisorEditAccount(self ):
        # assume user is supervisor

        result1 = a.command('edit their own address')
        self.assertEqual(result1, 'edit successfully')
            # Supervisor can edit their own address

        result2 = a.command('edit their own phone Number')
        self.assertEqual(result2, 'edit successfully')
            #Supervisor can edit their own phoneNumber

        result3= a.command('edit their own email address')
        self.assertEqual(result3, 'edit successfully')
            #Supervisor can edit their own emailAddress

        result4= a.command('edit their own userName')
        self.assertEqual(result4, 'edit successfully')
            #Supervisor can edit their own username

        result5 = a.command('edit their password')
        self.assertEqual(result5, 'edit successfully')
            #Supervisor can edit their own password

            #What supervisor can edit on TA's account

        result6 = a.command('edit TA address')
        self.assertEqual(result6, 'edit successfully')
            # supervisor can edit TA's address

        result7 = a.command('edit TA phone number')
        self.assertEqual(result7, 'edit successfully')
            # supervisor can edit TA's phoneNumber

        result8= a.command('edit TA email address')
        self.assertEqual(result8, 'edit successfully')
            #Supervisor can edit TA's emailAddress

        result9= a.command('edit their supervisor userName')
        self.assertEqual(result9, 'edit unsuccessful')
            #Supervisor can not edit TA's username

        result10 = a.command('edit their password')
        self.assertEqual(result10, 'edit unsuccessful')
            #can edit can not edit TA's password

            #What supervisor can edit on Admin Account

        result11 = a.command('edit admin address')
        self.assertEqual(result11, 'edit successfully')
            # supervisor can edit Admin's address

        result12 = a.command('edit admin phone Number')
        self.assertEqual(result12, 'edit successfully')
            # supervisor can edit Admin's phoneNumber

        result13 = a.command('edit admin email address')
        self.assertEqual(result13, 'edit successfully')
            #Supervisor can edit Admin's emailAddress

        result14= a.command('edit their supervisor userName')
        self.assertEqual(result14, 'edit unsuccessful')
            #Supervisor can not edit Admin's username

        result15 = a.command('edit their password')
        self.assertEqual(result15, 'edit unsuccessful')
            #supervisor can not edit Admin's password

            #What supervisor can edit on student's Account

        result16 = a.command('edit  student address')
        self.assertEqual(result16, 'edit successfully')
            # supervisor can edit student's address

        result17 = a.command('edit student phone Number')
        self.assertEqual(result17, 'edit successfully')
            # supervisor can edit student's phoneNumber

        result18 = a.command('edit student email address')
        self.assertEqual(result18, 'edit successfully')
            #Supervisor can edit student's emailAddress

        result19= a.command('edit their supervisor userName')
        self.assertEqual(result19, 'edit unsucessful')
            #Supervisor can not edit student's username

        result20 = a.command('edit their password')
        self.assertEqual(result20, 'edit unsucessful')
            #Supervisor can not edit student's password

            #What supervisor can edit on Instructor's Account

        result21 = a.command('edit  Instructor address')
        self.assertEqual(result21, 'edit successfully')
            # supervisor can edit instructor's address

        result22 = a.command('edit Instructor phone Number')
        self.assertEqual(result22, 'edit successfully')
            # supervisor can edit instructor's phoneNumber

        result23 = a.command('edit Instructor email address')
        self.assertEqual(result23, 'edit successfully')
            #Supervisor can edit instructor's emailAddress

        result24= a.command('edit their supervisor userName')
        self.assertEqual(result24, 'edit unsucessful')
            #Supervisor can not edit instructor's username

        result25 = a.command('edit instructor password')
        self.assertEqual(result25, 'edit unsucessful')
            #Supervisor can not edit instructor's password

    def test_supervisorEditCourse(self):
        # assume user is supervisor

        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit successfully')
            # can edit courses

    def test_AdminEditAccount(self):
            # assume user is Admin

        result1 = a.command('edit their own address')
        self.assertEqual(result1, 'edit successfully')
            # Admin can edit their own address

        result2 = a.command('edit their own phone Number')
        self.assertEqual(result2, 'edit successfully')
            #Admin can edit theri own phoneNumber

        result3= a.command('edit their own email address')
        self.assertEqual(result3, 'edit successfully')
            #Admin can edit their own emailAddress

        result4= a.command('edit their own userName')
        self.assertEqual(result4, 'edit successfully')
            #Admin can edit their own username

        result5 = a.command('edit their password')
        self.assertEqual(result5, 'edit successfully')
            #Admin can edit their own password

            #What Admin can edit on TA's account

        result6 = a.command('edit TA address')
        self.assertEqual(result6, 'edit successfully')
            # Admin can edit TA's address

        result7 = a.command('edit TA phone number')
        self.assertEqual(result7, 'edit successfully')
            # Admin can edit TA's phoneNumber

        result8= a.command('edit TA email address')
        self.assertEqual(result8, 'edit successfully')
            #Admin can edit TA's emailAddress

        result9= a.command('edit their supervisor userName')
        self.assertEqual(result9, 'edit unsucessful')
            #Admin can not edit TA's username

        result10 = a.command('edit their password')
        self.assertEqual(result10, 'edit unsucessful')
            #Admin  can not edit TA's password

            #What Admin can edit on other Admin's Account

        result11 = a.command('edit admin address')
        self.assertEqual(result11, 'edit unsucessful')
             #  Admin can not edit other Admin's address

        result12 = a.command('edit admin phone Number')
        self.assertEqual(result12, 'edit unsucessful')
            # Admin can not edit other Admin's phoneNumber

        result13 = a.command('edit admin email address')
        self.assertEqual(result13, 'edit unsucessful')
            #Admin can not edit other Admin's emailAddress

        result14= a.command('edit their supervisor userName')
        self.assertEqual(result14, 'edit unsucessful')
            #Admin can not edit other Admin's username

        result15 = a.command('edit their password')
        self.assertEqual(result15, 'edit unsucessful')
            #Admin can not edit other Admin's password

            #What Admin can edit on student's Account

        result16 = a.command('edit  student address')
        self.assertEqual(result16, 'edit successfully')
            # Admin can edit student's address

        result17 = a.command('edit student phone Number')
        self.assertEqual(result17, 'edit successfully')
            # Admin can edit student's phoneNumber

        result18 = a.command('edit student email address')
        self.assertEqual(result18, 'edit successfully')
            #Admin can edit student's emailAddress

        result19= a.command('edit their supervisor userName')
        self.assertEqual(result19, 'edit unsucessful')
            #Admin can not edit student's username

        result20 = a.command('edit their password')
        self.assertEqual(result20, 'edit unsucessful')
            #Admin can not edit student's password

        #What Admin can edit on Instructor's Account

        result21 = a.command('edit  Instructor address')
        self.assertEqual(result21, 'edit successfully')
            # Admin can edit instructor's address

        result22 = a.command('edit Instructor phone Number')
        self.assertEqual(result22, 'edit successfully')
            # Admin can edit instructor's phoneNumber

        result23 = a.command('edit Instructor email address')
        self.assertEqual(result23, 'edit successfully')
            # Admin can edit instructor's emailAddress

        result24= a.command('edit their supervisor userName')
        self.assertEqual(result24, 'edit unsucessful')
            # Admin can not edit instructor's username

        result25 = a.command('edit instructor password')
        self.assertEqual(result25, 'edit unsucessful')
            # Admin can not edit instructor's password

            #What Admin can edit on Supervisor Account

        result26 = a.command('edit admin address')
        self.assertEqual(result26, 'edit unsucessful')
            #  Admin can not edit supervisor's address

        result27 = a.command('edit admin phone Number')
        self.assertEqual(result27, 'edit unsucessful')
            # Admin can not edit supervisor's phoneNumber

        result28 = a.command('edit admin email address')
        self.assertEqual(result28, 'edit unsucessful')
            #Admin can not edit supervisor's emailAddress

        result29= a.command('edit their supervisor userName')
        self.assertEqual(result29, 'edit unsucessful')
            #Admin can not edit supervisor'susername

        result30 = a.command('edit their password')
        self.assertEqual(result30, 'edit unsucessful')
            #Admin can not edit supervisor's password


    def test_AdminEditCourse(self):
        # assume user is Admin
        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit successfully')
            # can edit courses

    def test_taEditAccount(self):
        # assume user is TA

        result1 = a.command('edit their own address')
        self.assertEqual(result1, 'edit successfully')
        # TA can edit their own address

        result2 = a.command('edit their own phone Number')
        self.assertEqual(result2, 'edit successfully')
        #TA can edit their own phoneNumber

        result3= a.command('edit their own email address')
        self.assertEqual(result3, 'edit successfully')
        #TA can edit their own emailAddress

        result4= a.command('edit their own userName')
        self.assertEqual(result4, 'edit successfully')
        #TA can edit their own username

        result5 = a.command('edit their password')
        self.assertEqual(result5, 'edit successfully')
        #TA can edit their own password

        #What TA can edit on other TA's account

        result6 = a.command('edit TA address')
        self.assertEqual(result6, 'edit unsucessful')
        # TA can not edit TA's address

        result7 = a.command('edit TA phone number')
        self.assertEqual(result7, 'edit unsucessful')
        # TA can not edit TA's phoneNumber

        result8= a.command('edit TA email address')
        self.assertEqual(result8, 'edit unsucessful')
        # TA can not edit other TA's emailAddress

        result9= a.command('edit their supervisor userName')
        self.assertEqual(result9, 'edit unsucessful')
        # TA can not edit other TA's username

        result10 = a.command('edit their password')
        self.assertEqual(result10, 'edit unsucessful')
        # TA can not edit other TA's password

        #What TA can edit on Admin's Account

        result11 = a.command('edit admin address')
        self.assertEqual(result11, 'edit unsucessful')
        #  TA can not edit other Admin's address

        result12 = a.command('edit admin phone Number')
        self.assertEqual(result12, 'edit unsucessful')
        # TA can not edit other Admin's phoneNumber

        result13 = a.command('edit admin email address')
        self.assertEqual(result13, 'edit unsucessful')
        # TA can not edit other Admin's emailAddress

        result14= a.command('edit their supervisor userName')
        self.assertEqual(result14, 'edit unsucessful')
        # TA can not edit other Admin's username

        result15 = a.command('edit their password')
        self.assertEqual(result15, 'edit unsuccessful')
        # TA can not edit other Admin's password

        #What Admin can edit on student's Account

        result16 = a.command('edit  student address')
        self.assertEqual(result16, 'edit unsuccessful')
        # TA can not edit student's address

        result17 = a.command('edit student phone Number')
        self.assertEqual(result17, 'edit unsuccessful')
        # TA can not edit student's phoneNumber

        result18 = a.command('edit student email address')
        self.assertEqual(result18, 'edit unsuccessful')
        # TA can not edit student's emailAddress

        result19= a.command('edit their supervisor userName')
        self.assertEqual(result19, 'edit unsuccessful')
        # TA can not edit student's username

        result20 = a.command('edit their password')
        self.assertEqual(result20, 'edit unsuccessful')
        # TA can not edit student's password

        #What Admin can edit on Instructor's Account

        result21 = a.command('edit  Instructor address')
        self.assertEqual(result21, 'edit unsuccessful')
        # TA can not edit instructor's address

        result22 = a.command('edit Instructor phone Number')
        self.assertEqual(result22, 'edit unsuccessful')
        # TA can not edit instructor's phoneNumber

        result23 = a.command('edit Instructor email address')
        self.assertEqual(result23, 'edit unsuccessful')
        # TA can not edit instructor's emailAddress

        result24= a.command('edit their supervisor userName')
        self.assertEqual(result24, 'edit unsuccessful')
        # TA can not edit instructor's username

        result25 = a.command('edit instructor password')
        self.assertEqual(result25, 'edit unsuccessful')
        # TA can not edit instructor's password

        #What TA can edit on Supervisor Account

        result26 = a.command('edit admin address')
        self.assertEqual(result26, 'edit unsuccessful')
        #  TA can not edit supervisor's address

        result27 = a.command('edit admin phone Number')
        self.assertEqual(result27, 'edit unsuccessful')
        # TA can not edit supervisor's phoneNumber

        result28 = a.command('edit admin email address')
        self.assertEqual(result28, 'edit unsuccessful')
        # TA can not edit supervisor's emailAddress

        result29= a.command('edit their supervisor userName')
        self.assertEqual(result29, 'edit unsuccessful')
        # TA can not edit supervisor's username

        result30 = a.command('edit their password')
        self.assertEqual(result30, 'edit unsuccessful')
        # TA can not edit supervisor's password


    def test_taEditCourse(self):
        # assume user is TA
        result= a.command('edit course successfully')
        self.assertEqual(result, 'edit unsuccessful')
            # can't  edit courses

    def test_instructorEditAccount(self):
        # assume user is Instructors

        result1 = a.command('edit their own address')
        self.assertEqual(result1, 'edit successfully')
            # Instructor can edit their own address

        result2 = a.command('edit their own phone Number')
        self.assertEqual(result2, 'edit successfully')
            # Instructor can edit their own phoneNumber

        result3= a.command('edit their own email address')
        self.assertEqual(result3, 'edit successfully')
            # Instructor can edit their own emailAddress

        result4= a.command('edit their own userName')
        self.assertEqual(result4, 'edit successfully')
            # Instructor can edit their own username

        result5 = a.command('edit their password')
        self.assertEqual(result5, 'edit successfully')
            # Instructor can edit their own password

            #What Instructor can edit on TA's account

        result6 = a.command('edit TA address')
        self.assertEqual(result6, 'edit unsuccessful')
            # Instructor can edit TA's address

        result7 = a.command('edit TA phone number')
        self.assertEqual(result7, 'edit unsuccessful')
            # Instructor can not edit TA's phoneNumber

        result8= a.command('edit TA email address')
        self.assertEqual(result8, 'edit unsuccessful')
            # Instructor can not edit TA's emailAddress

        result9= a.command('edit their supervisor userName')
        self.assertEqual(result9, 'edit unsuccessful')
            # Instructor can not edit TA's username

        result10 = a.command('edit their password')
        self.assertEqual(result10, 'edit unsuccessful')
            # Instructor can not edit  TA's password

            #What Instructor can edit on Admin's Account

        result11 = a.command('edit admin address')
        self.assertEqual(result11, 'edit unsuccessful')
            #  Instructor can not edit Admin's address

        result12 = a.command('edit admin phone Number')
        self.assertEqual(result12, 'edit unsuccessful')
            # Instructor can not edit Admin's phoneNumber

        result13 = a.command('edit admin email address')
        self.assertEqual(result13, 'edit unsuccessful')
            # Instructor can not edit Admin's emailAddress

        result14= a.command('edit their supervisor userName')
        self.assertEqual(result14, 'edit unsuccessful')
            # Instructor can not edit Admin's username

        result15 = a.command('edit their password')
        self.assertEqual(result15, 'edit unsuccessful')
            # Instructor can not edit Admin's password

            #What Instructor can edit on student's Account

        result16 = a.command('edit  student address')
        self.assertEqual(result16, 'edit unsuccessful')
            # Instructor can not edit student's address

        result17 = a.command('edit student phone Number')
        self.assertEqual(result17, 'edit unsuccessful')
            # Instructor can not edit student's phoneNumber

        result18 = a.command('edit student email address')
        self.assertEqual(result18, 'edit unsuccessful')
            # Instructor can not edit student's emailAddress

        result19= a.command('edit their supervisor userName')
        self.assertEqual(result19, 'edit unsuccessful')
            # Instructor can not edit student's username

        result20 = a.command('edit their password')
        self.assertEqual(result20, 'edit unsuccessful')
            # Instructor can not edit student's password

            #What Instructor can edit on other Instructor's Account

        result21 = a.command('edit  Instructor address')
        self.assertEqual(result21, 'edit unsuccessful')
            # Instructor can  notedit other instructor's address

        result22 = a.command('edit Instructor phone Number')
        self.assertEqual(result22, 'edit unsuccessful')
            # Instructor can not edit other instructor's phoneNumber

        result23 = a.command('edit Instructor email address')
        self.assertEqual(result23, 'edit unsuccessful')
            # Instructor can not edit other instructor's emailAddress

        result24= a.command('edit their supervisor userName')
        self.assertEqual(result24, 'edit unsuccessful')
            # Instructor can not edit other instructor's username

        result25 = a.command('edit instructor password')
        self.assertEqual(result25, 'edit unsuccessful')
            # Instructor can not edit other instructor's password

            #What Instructor can edit on Supervisor Account

        result26 = a.command('edit admin address')
        self.assertEqual(result26, 'edit unsuccessful')
            #  Instructor can not edit supervisor's address

        result27 = a.command('edit admin phone Number')
        self.assertEqual(result27, 'edit unsuccessful')
            # Instructor can not edit supervisor's phoneNumber

        result28 = a.command('edit admin email address')
        self.assertEqual(result28, 'edit unsuccessful')
            # Instructor can not edit supervisor's emailAddress

        result29= a.command('edit their supervisor userName')
        self.assertEqual(result29, 'edit unsuccessful')
            # Instructor can not edit supervisor's username

        result30 = a.command('edit their password')
        self.assertEqual(result30, 'edit unsuccessful')
            # Instructor can not edit supervisor's password


    def test_instructorsEditCourse(self):
        # assume user is Instructors
        result= a.command('edit courses ')
        self.assertEqual(result, 'edit unsuccessful')
            # can't edit courses

if __name__ == '__main__':

    bk.main()
