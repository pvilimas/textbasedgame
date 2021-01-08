from item import Item
from room import Room
from initialize import initializeManual
import settings
roomList = initializeManual()

inventory = []  # implement later

progression = {
    'completed': [],
    'remaining': [],
    'next': []  # set this to remaining[0] every turn
}

# methods for debugging only


def showDestinations(room):
    #print('Available Rooms:')
    for k in room.destinations.keys():
        if room.destinations[k] is not None:
            print(
                f'{settings.abbrDirections[k]} - {roomList[room.destinations[k]].name}')


def showItems(room):
    print('Items:')
    if len(room.itemList) == 0:
        print('No items')
        return
    for i in room.itemList:
        print(f'{i}')


currentRoomID = 0
currentRoom = roomList[currentRoomID]

movedThisTurn = True

# later on, change this to GUI/pygame based


def display(text):
    print(f'\n> {text}\n')


def processCommand(c):

    def itemCommandCheck(c):
        for item in currentRoom.itemList:
            try:
                if c == f'{item.kwUse} {item.name}':
                    item.use()
                    display(item.msgOnUse)
                    return True
            except:
                pass
        return False

    def gameCommandCheck(c):
        # pass the full command to this: like "use rope"
        if c in settings.lookAroundCmds:
            display(currentRoom.msgOnLook)
            return True
        # there will be more commands later and more things in the if/else chain here later (like seeing the inventory contents)
        return False

    def movementCommandCheck(dir):
        global roomList, currentRoom, currentRoomID, movedThisTurn
        movedThisTurn = False

        def move(dir):
            global roomList, currentRoom, currentRoomID, movedThisTurn
            if(currentRoom.destinations[dir] is not None):
                currentRoomID = currentRoom.destinations[dir]
                currentRoom = roomList[currentRoomID]
                display(f'You went {str(dir)}. ')
                movedThisTurn = True
            else:
                display(
                    f'You tried to go {str(dir)}. {settings.errorMsg + currentRoom.msgOnStay}')
                movedThisTurn = False

        for inputList in settings.inputModes:
            if dir in inputList:
                dir = inputList[0]
                break

        try:
            if(currentRoom.destinations[dir] is not None):
                currentRoomID = currentRoom.destinations[dir]
                currentRoom = roomList[currentRoomID]
                display(f'You went {str(dir)}. ')  # CUSTOMIZE THIS LATER
                movedThisTurn = True
                return True
            else:
                # if there is just no room in the direction, but if the dir is valid
                display(
                    f'You tried to go {str(dir)}. {settings.invalidDirMsg}')
                movedThisTurn = False
                return False
        except KeyError:
            # if the player inputs some shit like asjbdahs for the direction
            display(settings.invalidCmdMsg)

    if not itemCommandCheck(c):
        if not gameCommandCheck(c):
            if not movementCommandCheck(c):
                pass
            else:
                try:
                    global movedThisTurn
                    newDir = c
                except AttributeError:
                    newDir = None
                movedThisTurn = False
                try:
                    move(newDir.replace('\n', ''))
                except:
                    pass

# ------- MAIN GAME LOOP ------- #


crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    # showItems(currentRoom)
    # showDestinations(currentRoom)
    processCommand(input(f'> {currentRoom.msgOnEnter}\n> ')) if movedThisTurn else processCommand(
        input(f'> {currentRoom.msgOnStay}\n> '))


# ------- MAIN GAME LOOP ------- #
