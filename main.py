from item import Item
from room import Room
from initialize import randomizeRooms, randomizeRoomsNonRect, initializeManual
import settings
# wqetq
roomList = initializeManual()

def showDestinations(room):
    print('{}:'.format(room.ID))
    for k in room.destinations.keys():
        print(room.destinations[k])

#grid based test methods, will not be used
"""def showRooms():
    s = ""
    for row in range(len(roomGrid)):
        for col in range(len(roomGrid[row])):
            room = roomGrid[row][col]
            if (room is not None):
                s += '{:shorter} '.format(room)
            else:
                s += 'None'.ljust(18, ' ')
        s += "\n"
    print(s)


def showRoom(row, col):
    if(roomGrid[row][col] is not None):
        print('{:short}'.format(roomGrid[row][col]))
    else:
        print('None')"""

currentRoomID = 0
currentRoom = roomList[currentRoomID]

#later on, change this to GUI/pygame based
def display(text):
    print("\n> {}\n".format(text))

def move(dir):
    global roomList, currentRoom, currentRoomID, movedThisTurn
    if(currentRoom.destinations[dir] is not None):
        currentRoomID = currentRoom.destinations[dir]
        currentRoom = roomList[currentRoomID]
        display("You went " + str(dir) + ". ")
        movedThisTurn = True
    else:
        display("You went " + str(dir) + ". " +
                settings.errorMsg + currentRoom.msgOnStay)
        movedThisTurn = False

# ------- MAIN GAME LOOP ------- #

movedThisTurn = True
crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    showDestinations(currentRoom)
    try:
        newDir = input("> {}\n".format(currentRoom.msgOnEnter)) if (
            movedThisTurn and currentRoom is not None) else input("> ")
    except AttributeError:
        newDir = None
    movedThisTurn = False
    try:
        move(newDir.replace("\n", ""))
    except KeyError:
        display(settings.invalidDirMsg)
    except AttributeError:
        pass

# ------- MAIN GAME LOOP ------- #
