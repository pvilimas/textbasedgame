from item import Item
from room import Room
from randomize import randomizeRooms
import settings

roomList, roomGrid = randomizeRooms()

def showDestinations(room):
    print ("{}:".format(room.ID))
    for k in room.destinations.keys():
        print(room.destinations[k])

def showRooms():
    s = ""
    for row in range(len(roomGrid)):
        for col in range(len(roomGrid[row])):
            room = roomGrid[row][col]
            s += "{}".format(room)
        s += "\n"
    print(s)

currentRoomID = 0
currentRoom = None

def display(text):
    print("\n> {}\n".format(text))

def move(dir):
    global roomList, currentRoom, currentRoomID
    if(currentRoom.destinations[dir] is not None):
        currentRoomID = currentRoom.destinations[dir]
        currentRoom = roomList[currentRoomID]
        display("You went " + str(dir) + ". ")
    else:
        display("You went " + str(dir) + ". " + settings.errorMsg + currentRoom.msgOnStay)

crashed = False
while not crashed:
    currentRoom = roomList[currentRoomID]
    # showDestinations(currentRoom)
    showRooms()
    newDir = input("> {}\n".format(currentRoom.msgOnEnter))
    try:
        move(newDir.replace("\n", ""))
    except KeyError:
        display(settings.invalidDirMsg)
