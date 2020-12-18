from item import Item
from room import Room
import settings
from random import shuffle, choice
from copy import deepcopy
from math import sqrt, ceil, floor

roomList = []


def initializeManual():
    global roomList
    # assuming we want to use all room names in that list
    roomList = [Room(name, i) for i, name in enumerate(settings.possibleRoomNames)]
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


def linkRooms(a, b, dir):  # dir = direction from a to b
    # for one way passages, do not use this and simply assign one of the rooms manually but not the other
    # accepts ints for a, b or room objs but must be set to rooms when the program rly starts
    # if (isinstance(a, int) and isinstance(b, int)) else a, b - not needed
    a, b = roomList[a], roomList[b]
    # print(type(a))
    # set the inverse first
    if dir == "North":
        b.destinations["South"] = a.ID
    elif dir == "South":
        b.destinations["North"] = a.ID
    elif dir == "East":
        b.destinations["West"] = a.ID
    elif dir == "West":
        b.destinations["East"] = a.ID
    elif dir == "Northeast":
        b.destinations["Southwest"] = a.ID
    elif dir == "Southeast":
        b.destinations["Northwest"] = a.ID
    elif dir == "Northwest":
        b.destinations["Southeast"] = a.ID
    elif dir == "Southwest":
        b.destinations["Northeast"] = a.ID
    else:
        pass  # not sure what to put here
    # set the dir from A to B, avoid invalid key error
    try:
        a.destinations[dir] = b.ID
    except KeyError:
        pass


def getRoom(input, rl):  # rl = roomlist
    if type(input) is int:  # an ID
        return rl[input]
    elif type(input) is str:  # a name
        for r in rl:
            if r.name == input:
                return r
        else:
            raise Exception

def addItemToRoom(r, i):
    r.itemList.append(i)