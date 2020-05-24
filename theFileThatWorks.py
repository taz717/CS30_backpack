'''
Moataz Khallaf A.K.A Hackerman
Backpack
4/14/2019
'''

# Classes

class storage:
    def __init__(self, name):
        self.items = []
        self.name = name

    def __repr__(self):
        return self.items

    def __str__(self):
        return self.items

    def getName(self):
        return self.name

    def getItems(self):
        return self.items

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        for i in range(len(self.items)):
            if item in self.items[i].getObjectName():
                self.items.pop(i)

    def printList(self):
        print(self.name)
        for i in range(len(self.items)):
            print(self.items[i].getObjectName())

class stationary:
    def __init__(self, name):
        self.name = name
        self.colour = None
        self.fit = 1

    def setColour(self, colour):
        self.colour = colour

    def __str__(self):
        return self.colour + " " + self.name

    def getObject(self):
        return self.name

    def getObjectName(self):
        return self.colour + " " + self.name


# Functions
def menu():
    locker.printList()  # shows items for all storage devices
    backpack.printList()
    case.printList()


    x = int(input('''
    1) add an item
    2) swap an item from storage devices
    3) exit
    '''))

    return x

# Main Code


locker = storage("locker")
case = storage("pencilcase")
backpack = storage("backpack")

storage = [locker, backpack, case]


while True:
    choice = menu()

    if choice == 1:  # create item
        item = stationary(input("name "))
        item.setColour(input("colour"))

        x = int(input(f''' please pick which storage device it's in
                1) {locker.getName()}
                2) {case.getName()}
                3) {backpack.getName()}
                '''))

        x -= 1
        storage[x].addItem(item)

    elif choice == 2:  # swap item
        x = int(input(f''' please pick which storage device it's in
        1) {locker.getName()}
        2) {backpack.getName()}
        3) {case.getName()}

        '''))
        y = int(input(f''' please pick which storage you want it to be in
        1) {locker.getName()}
        2) {backpack.getName()}
        3) {case.getName()}
        '''))

        y -= 1  # changes it so the choice pics from the array
        x -= 1  # this is done to avoid having like a billion if statements

        storage[x].printList()
        z = int(input("What is the item you wish to move?"))

        z -= 1  # lol off by one error ...

        print(storage[x].items)

        storage[y].items.append(storage[x].items.pop(z))

    if choice == 3:
        exit()