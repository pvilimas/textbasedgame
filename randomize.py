from item import Item
from room import Room
import settings
from random import shuffle
from copy import deepcopy

def randomizeRooms():
    roomList = []
    possibleRoomNames = ["Library", "Kitchen", "Terrace", "Fountain", "Engine Room", "Garden", "Bedroom", "AP Office", "YSR Headquarters"]
    shuffledList = deepcopy(possibleRoomNames)
    shuffle(shuffledList)
    for i in range(0, len(possibleRoomNames)):
        roomList.append(Room(shuffledList[i], i, []))
    roomListCopy = deepcopy(roomList)
    shuffle(roomListCopy)
    roomGrid = [roomListCopy[0:3], roomListCopy[3:6], roomListCopy[6:9]]
    # north = row-1, south = row+1, west = col-1, east = col+1
    for row in range(len(roomGrid)):
        for col in range(len(roomGrid[row])):
            try:
                if (row-1 < 0):
                    raise ValueError
                roomGrid[row][col].destinations["North"] = roomGrid[row-1][col].ID
            except ValueError:
                pass
            try:
                roomGrid[row][col].destinations["South"] = roomGrid[row+1][col].ID
            except IndexError:
                pass
            try:
                roomGrid[row][col].destinations["East"] = roomGrid[row][col+1].ID
            except IndexError:
                pass
            try:
                if (col-1 < 0):
                    raise ValueError
                roomGrid[row][col].destinations["West"] = roomGrid[row][col-1].ID
            except ValueError:
                pass

    finalList = []
    for i in range(len(roomGrid)):
        finalList += roomGrid[i]

    return finalList, roomGrid #test
