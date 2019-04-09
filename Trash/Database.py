from Skeleton_Classes.App import *



class Database(object):
   # _commands = ['parse', 'set_pointer_to_app', 'login', 'create', 'notify', 'assign', 'logout', 'edit', 'access',
   #              'delete', 'assignments', 'verify']

    def read(self, readTable, *readQuery):

        app = App()

        # Parse user input
        input_list = self.parse(user_input)
        user_command = input_list[0]

        # Compare command to list of commands to find a match
            # If command matches one of the commands from the list
        if user_command in self._commands:
                # Perform the command
            return app.command(user_command)
        else:
            return "Command does not exist"


    def write(self,database, target):
        event=self.edit(database,target)
        event.save()
