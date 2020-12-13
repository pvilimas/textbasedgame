from item import Item
from room import Room
import settings
from random import shuffle, choice
from copy import deepcopy
from math import sqrt, ceil, floor
        
roomList = []

def initializeManual():
    global roomList
    roomList = [Room(name, i, []) for i, name in enumerate(settings.possibleRoomNames)]
    for r in roomList:
        print('{:short}'.format(r))

    linkRooms(0, 1, "South")
    linkRooms(0, 2, "East")
    linkRooms(0, 8, "West")
    linkRooms(8, 5, "South")
    linkRooms(1, 7, "East")
    linkRooms(7, 4, "East")
    linkRooms(2, 6, "North")
    linkRooms(2, 3, "East")
    linkRooms(3, 4, "South")

    return roomList

def linkRooms(a, b, dir): #dir = direction from a to b
    #accepts ints for a, b or room objs but must be set to rooms when the program rly starts
        a, b = roomList[a], roomList[b] # if (isinstance(a, int) and isinstance(b, int)) else a, b - not needed
        # print(type(a))
    #set the inverse first
        if dir == "North":
            b.destinations["South"] = a.ID
        elif dir == "South":
            b.destinations["North"] = a.ID
        elif dir == "East":
            b.destinations["West"] = a.ID
        elif dir == "West":
            b.destinations["East"] = a.ID
        else:
            pass #not sure what to put here
        #set the dir from A to B, avoid invalid key error
        try:
            a.destinations[dir] = b.ID
        except KeyError:
            pass

def getRoom(input, rl): #rl = roomlist
        if type(input) is int: # an ID
            return rl[input]
        elif type(input) is str: # a name
            for r in rl:
                if r.name == input:
                    return r
            else:
                raise Exception

def randomizeRoomsNonRect(): #do not use this
    roomList = []
    possibleRoomNames = settings.possibleRoomNames
    shuffledNameList = deepcopy(possibleRoomNames)
    shuffle(shuffledNameList)
    # height and width of a square grid
    gridSize = ceil(sqrt(len(possibleRoomNames))) + 2
    roomGrid = []
    roomList = []
    for i in range(len(possibleRoomNames)):
        roomList.append(Room(shuffledNameList[i], i, []))

    for i in range(gridSize):
        roomGrid.append([])
        for j in range(gridSize):
            roomGrid[i].append(None)

    openTiles = []  # a list of (row, col) tuples corresponding to grid squares
    openTiles.append((floor(gridSize/2), floor(gridSize/2)))
    for room in roomList:
        currentTile = choice(openTiles)
        openTiles.pop(openTiles.index(currentTile))
        row = currentTile[0]
        col = currentTile[1]
        roomGrid[row][col] = room
        for v in settings.borderingTileVectors:
            rowV = row + v[0]
            colV = col + v[1]
            if(rowV < 0 or rowV >= gridSize or colV < 0 or colV >= gridSize):  # establish bounds
                continue
            openTiles.append((rowV, colV))
            openTiles = list(set(openTiles))

            targetRoom = roomGrid[rowV][colV]
            if targetRoom is not None:
                room.destinations[settings.directionDict[v]] = targetRoom.ID
    startingRoomID = roomGrid[floor(gridSize/2)][floor(gridSize/2)].ID
    return roomList


def randomizeRooms():  # old method will not be used
    roomList = []
    possibleRoomNames = settings.possibleRoomNames
    shuffledNameList = deepcopy(possibleRoomNames)
    shuffle(shuffledNameList)
    for i in range(len(possibleRoomNames)):
        roomList.append(Room(shuffledNameList[i], i, []))
    roomGrid = [roomList[0:3], roomList[3:6], roomList[6:9]]
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

    return finalList, roomGrid
