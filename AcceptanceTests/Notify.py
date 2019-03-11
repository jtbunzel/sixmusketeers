import unittest as bk


class TestNotify(bk):
    # assume user exists
    # assume user is logged in
    # assume sender are Supervsiro/Admin/Instructor


    def test_message(self):
        # assume message is not empty
        # assume receiver has UWm email
        a= App
        result = a.command('sending message ')
        # will fail:
        #           if sent to non wum email address
        #           if email doesn't exit
        #           if TA attempts to send notification
        self.assertEqual(result, 'Notify successfully')

    def test_emptyMessage(self):
        # assume receiver has UWm email
        a=App()
        result= a.command('sending empty message')
        self.assertEqual(result, 'cannot notify empty message')

    def test_uwmemail(self):
        a=App()
        # assume message is not empty
        result= a.command('sending message to uwm email')
        self.assertEqual(result, 'Notify successfully')

    def test_nonuwmemail(self):
        # assume message is not empty
        a=App()
        result=a.command('sending message to non-uwm email')
        # fail:- non uwm email
        self.assertEqual(result,'notify unsuccessful, invalid email address')

    def test_TA_as_notifer(self):
        a=App()
        # assume message is not empty
        # assume email address is valid
        result= a.command('TA sending message')
        self.assertEqual(result,'not authorized to send notification')

if __name__ == '__main__':
    bk.main()