import unittest as bk


class TestNotify(bk):
    # assume user exists
    # assume user is logged in
    # assume receiver has UWM email address
    # assume sender are Supervsiro/Admin/Instructor
    a= app()

    def test_message():
        # assume message is not empty
        # assume receiver has UWm email
        result = a.command('sending message ')
        self.assertEqual(result, 'Notify successfully')

    def test_emptyMessage():
        # assume receiver has UWm email
        result= a.command('sending empty message')
        self.assertEqual(result, 'Notify unsuccessful')

    def test_uwmemail():
        # assume message is not empty
        result= a.command('sending message to uwm email')
        self.assertEqual(result, 'Notify successfully')

    def test_nonuwmemail():
        # assuem message is not empty
        result=a.command('sending message to non uwm email')
        self.assertEqual(result,'notify unsuccessful')

if __name__ == '__main__':
    bk.main()