from item import Item
from room import Room
from randomize import randomizeRooms, randomizeRoomsNonRect
import settings

roomList, roomGrid, startingRoomID = randomizeRoomsNonRect()

"""
    options/checklist for tomorrow/in general (move function):
    1) get rid of room.destinations and rely on the grid entirely
    2) revert back to the old way and dont move directly in the grid but with room.dest (for this to work, the grid has to be synced with every single dest dictionary)
    
    then fix all bugs (there's a lot)
    then implement items maybe (start by randomizing)
    then add item types (keys, doors, etc)
    then add text overrides ("you used the key" "you turned on the light" "you walked down the stairs" "you turned left and went into the cellar)
        probably by manually setting the var for each room that needs it
    at some point, setup pygame shit and change display method to GUI
        text scrolling would be needed, maybe a custom textbox class
    maybe hallways as special types of rooms (with a split path)
    add more directions to the dest array: NE NW SE SW
        what will be done with vertical rooms (climbing ladders/stairs to go up and down etc) 
    objectives - point counter for each item that is collected/used?
"""

def showDestinations(room):
    print('{}:'.format(room.ID))
    for k in room.destinations.keys():
        print(room.destinations[k])


def showRooms():
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
        print('None')


currentRoomID = startingRoomID
currentRoom = roomList[currentRoomID]


def display(text):
    print("\n> {}\n".format(text))


def getCoords(r):  # a room
    global roomGrid
    for i in range(len(roomGrid)):
        for j in range(len(roomGrid[i])):
            # print(i, j)
            if(roomGrid[i][j] is not None):
                if(roomGrid[i][j].ID == r.ID):
                    return i, j
                continue
    return 0, 0


def move(dir):
    row = col = 0
    """global roomList, currentRoom, currentRoomID, movedThisTurn
    if(currentRoom.destinations[dir] is not None):
        currentRoomID = currentRoom.destinations[dir]
        currentRoom = roomList[currentRoomID]
        display("You went " + str(dir) + ". ")
        movedThisTurn = True
    else:
        display("You went " + str(dir) + ". " + settings.errorMsg + currentRoom.msgOnStay)
        movedThisTurn = False"""

    global roomList, currentRoom, currentRoomID, movedThisTurn
    currentRoom = roomList[currentRoomID]
    v = settings.directionVectors[dir]
    row, col = getCoords(currentRoom)
    # print(f'{row+v[0]} {col+v[1]}')
    row, col = row + v[0], col + v[1]
    if (roomGrid[row][col] is not None):
        currentRoomID = currentRoom.destinations[dir].ID
        currentRoom = roomList[currentRoomID]
        display("You went " + str(dir) + ". ")
        movedThisTurn = True
    else:
        display("You went " + str(dir) + ". " +
                settings.errorMsg + currentRoom.msgOnStay)
        movedThisTurn = False

movedThisTurn = True
crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    # showDestinations(currentRoom)
    showRooms()
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
