from item import Item
from room import Room
from initialize import initializeManual
import settings

roomList = initializeManual()


def showDestinations(room):
    print(f'{room.ID}:')
    for k in room.destinations.keys():
        print(f'{k[0:1]} - {room.destinations[k]}')


currentRoomID = 0
currentRoom = roomList[currentRoomID]

# later on, change this to GUI/pygame based


def display(text):
    print(f'\n> {text}\n')


def processInput(i):
    for inputList in settings.inputModes:
        if i in inputList:
            return inputList[0]
    else:
        return i  # if i is invalid, this is fine and is better than raising an error


def move(dir):
    global roomList, currentRoom, currentRoomID, movedThisTurn
    if(currentRoom.destinations[dir] is not None):
        currentRoomID = currentRoom.destinations[dir]
        currentRoom = roomList[currentRoomID]
        display(f'You went {str(dir)}. ')
        movedThisTurn = True
    else:
        display(
            f'You went {str(dir)}. {settings.errorMsg + currentRoom.msgOnStay}')
        movedThisTurn = False

# ------- MAIN GAME LOOP ------- #


movedThisTurn = True
crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    showDestinations(currentRoom)
    try:
        newDir = processInput(input(f'> {currentRoom.msgOnEnter}\n')) if (
            movedThisTurn and currentRoom is not None) else input('> ')
    except AttributeError:
        newDir = None
    movedThisTurn = False
    try:
        move(newDir.replace('\n', ''))
    except KeyError:
        display(settings.invalidDirMsg)
    except AttributeError:
        pass

# ------- MAIN GAME LOOP ------- #
