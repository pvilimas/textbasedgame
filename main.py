from item import Item
from room import Room
from initialize import initializeManual
import settings
roomList, itemList = initializeManual()

inventory = itemList

progression = {  # do this much later
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


def showInventory():  # this one's gotta actually be detailed and look good bc it will be in the game
    global inventory
    display(
        f"Your inventory contains {' and '.join(repr(i) for i in inventory)}")


def lookAround():  # same here
    global currentRoom
    itemString = 'No items can be found here. ' if len(
        currentRoom.itemList) == 0 else f"The items that can be found here are: {' and '.join(repr(i) for i in currentRoom.itemList)}. "
    display(f'{currentRoom.msgOnLook}{itemString}')


currentRoomID = 0
currentRoom = roomList[currentRoomID]

movedThisTurn = True

# later on, change this to GUI/pygame based


def display(text):
    print(f'\n> {text}\n')


def pickUpItem(itemID):
    global currentRoom
    item = itemList[itemID]
    if not item.canBePickedUp or item not in currentRoom.itemList:
        raise settings.CannotTakeItemException
    else:
        inventory.append(itemID)


def dropItem(itemID):
    item = itemList[itemID]
    if item not in inventory:
        # maybe implicitly raise a value error here instead?
        raise settings.ItemNotInInventoryException
    else:
        inventory.remove(itemID)


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
            lookAround()
            return True
        elif c in settings.checkInvCmds:
            showInventory()
            return True
        # add other commands before this one (this should be the last in the chain)
        else:
            for item in currentRoom.itemList:
                # command should look like keyword + space + itemName: "use rope"
                for kw in item.keywords:
                    if c == f'{kw} {item.name}':
                        try:
                            if kw == 'use':
                                item.use()
                            elif kw == 'pick up':
                                pickUpItem(item.ID)
                            elif kw == 'drop':
                                dropItem(item.ID)
                            else:
                                return False  # is this ok?
                        except:  # might have to be more specific here later with diff error types
                            display(settings.invalidItemMsg)

        return False

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

    def movementCommandCheck(dir):
        global roomList, currentRoom, currentRoomID, movedThisTurn
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

    # ------- MAIN HIERARCHY ------- #

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
    # showInventory()
    processCommand(input(f'> {currentRoom.msgOnEnter}\n\n> ')) if movedThisTurn else processCommand(
        input(f'> {currentRoom.msgOnStay}\n\n> '))


# ------- MAIN GAME LOOP ------- #
