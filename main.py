from item import Item
from room import Room
from initialize import initializeManual
import settings
roomList = initializeManual()


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

# later on, change this to GUI/pygame based


def display(text):
    print(f'\n> {text}\n')


def processDirection(i):  # used for directions (capitalization)
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


movedThisTurn = True
crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    #showItems(currentRoom)
    #showDestinations(currentRoom)
    try:
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
        pass

# ------- MAIN GAME LOOP ------- #
