class Parser:

    def __init__(self):
        self.commands = Commands()
        self.last_command_called = None

    def parse(self, command_string):
        words = command_string.split(" ")

        i = 0
        self.commands.start()
        while self.commands.has_next():


