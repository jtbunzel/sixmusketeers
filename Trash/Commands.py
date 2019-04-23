class Commands():

    def __init__(self):
        self.listOfCommands = ['logout', 'createuser', 'deleteuser', 'editaccount',
                                'searchuser', 'showuser', 'showall']
        self.currentIndex = -1


    def start(self):
        self.currentIndex = -1

    def advance(self):
        self.currentIndex += 1
        return listOfCommands[self.currentIndex]

    def has_next(self):
        return self.currentIndex == self.listOfCommands.count() - 1

    def call(self, input):
        command = self.listOfCommands[self.currentIndex]

        if command == 'logout':
            UserCommandController.logout()
        if command == 'createUser':
            AdminSuperCommandController.createUser(input)
        if command == 'deleteuser':
            AdminSuperCommandController.deleteUser(input)
        if command == 'editAccount':
            UserCommandController.editAccount(input)
        if command == 'searchuser':
            UserCommandController.searchUser(input)
        if command == 'showuser':
            UserCommandController.showUser()
        if command == 'showall':
            SuperAdminCommandController.showAll()







