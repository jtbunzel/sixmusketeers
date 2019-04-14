class Parser:

    def __init__(self):
        self.commands = Commands()
        self.last_command_called = None

    def parse(self, command_string):
        words = command_string.split(" ")
        if(len(words)==0)
            raise Exception

        user_inputted_command = words[0]
        self.commands.start()

        while self.commands.has_next():
            nextCommand = self.command.next()
            if user_inputted_command == nextCommand:
                return Commands.call(words[1:])


        return "Command unknown."
