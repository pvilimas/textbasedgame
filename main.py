from item import Item
from room import Room
from initialize import initializeManual
import settings
roomList = initializeManual()

inventory = [] #implement later

progression = { #explain this to ab later
    'completed': [],
    'remaining': [],
    'next': [] # set this to remaining[0] every turn
}

def showDestinations(room):
    print(f'{room.ID}:')
    for k in room.destinations.keys():
        print(f'{k[0:1]} - {room.destinations[k]}')


def showItems(room):
    print(f'{room.ID}:')
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
    if not itemCommandCheck(c):
        if not gameCommandCheck(c):
            if not movementCommandCheck(c):
                print("invalid input!") #fix this pls
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
    if(currentRoom.destinations[dir] is not None):
        currentRoomID = currentRoom.destinations[dir]
        currentRoom = roomList[currentRoomID]
        display(f'You went {str(dir)}. ') #CUSTOMIZE THIS LATER
        movedThisTurn = True
        return True
    else:
        display(
            f'You tried to go {str(dir)}. {settings.invalidDirMsg + currentRoom.msgOnStay}')
        movedThisTurn = False
        return False

def processDirection(i):  # used for directions to get the version the program uses - "North" is better than "north" or "n"
    for inputList in settings.inputModes:
        if i in inputList:
            return inputList[0]
    else:
        return i  # if i is invalid, this is fine and is better than raising an error


# will be for stuff like using items or looking around in a room
def processGameCommand(c):
    # pass the full command to this: like "use rope"
    if c in settings.lookAroundCmds:
        display(currentRoom.msgOnLook)
    for item in currentRoom.itemList:
        if c == f'{item.keyword} {item.name}':
            item.use()
            display(item.msgOnUse)
    else:
        raise Exception


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

# ------- MAIN GAME LOOP ------- #


crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    showItems(currentRoom)
    #showDestinations(currentRoom)

    newDir = processCommand(input(f'> {currentRoom.msgOnEnter}\n')) if (
            movedThisTurn and currentRoom is not None) else input('> ')

    """try:
        newDir = processDirection(input(f'> {currentRoom.msgOnEnter}\n')) if (
            movedThisTurn and currentRoom is not None) else input('> ')
    except AttributeError:
        newDir = None
    movedThisTurn = False
    try:
        move(newDir.replace('\n', ''))
    except KeyError:
        try:
            processGameCommand("use rope")
        except:
            display(settings.invalidDirMsg)
    except:
        pass"""

# ------- MAIN GAME LOOP ------- #
