from item import Item
from room import Room
from initialize import initializeManual
import settings
roomList, itemList = initializeManual()

import pygame

GUIEnabled = False #maybe enable this in the actual game so people can decide to play from command line or GUI window lol

inventory = []

progression = {  # do this much later
    'completed': [],  # starts empty of course
    'remaining': [],  # once this is done, this list should be received as a return value from initializeManual
    'next': []  # set this to remaining[0] every turn
}

def addToInventory(item):
    global inventory
    inventory.append(item)

def removeFromInventory(item):
    global inventory
    inventory.remove(item)

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
        f"Your inventory contains {' and '.join(repr(i) for i in inventory)}.") if len(inventory) > 0 else display('Your inventory is empty.')


def lookAround():  # same here
    global currentRoom, lookedAroundThisTurn
    lookedAroundThisTurn = True
    itemString = 'No items can be found here. ' if len(
        currentRoom.itemList) == 0 else f"The items that can be found here are: {' and '.join(repr(i) for i in currentRoom.itemList)}. "  # just know that this works :)
    display(f'{currentRoom.msgOnLook}{itemString}')


currentRoomID = 0
currentRoom = roomList[currentRoomID]

movedThisTurn = True
lookedAroundThisTurn = False
itemMsgGivenThisTurn = False
invMsgGivenThisTurn = False

# later on, change this to GUI/pygame based


def display(text):
    print(f'\n> {text}\n')


def takeItem(itemID):
    global currentRoom
    item = itemList[itemID]
    if not item.canBePickedUp or item not in currentRoom.itemList:
        raise settings.CannotTakeItemException
    else:
        currentRoom.itemList.remove(item)
        inventory.append(item)
        display(item.msgOnTake)


def dropItem(itemID):
    print('dropping!')
    item = itemList[itemID]
    if item not in inventory:
        # maybe implicitly raise a value error here instead?
        raise settings.ItemNotInInventoryException
    else:
        currentRoom.itemList.append(item)
        inventory.remove(item)
        display(item.msgOnDrop)

# useItem does not exist, maybe it should but for now it's in the item class: item.use()
# and it returns the string to display


def processCommand(c):
    global lookedAroundThisTurn, itemMsgGivenThisTurn, invMsgGivenThisTurn
    lookedAroundThisTurn, itemMsgGivenThisTurn, invMsgGivenThisTurn = False, False, False

    # checks to see if user tried to use, drop, or take an item
    def itemCommandCheck(c):
        global itemList, inventory, itemMsgGivenThisTurn
        itemMasterList = itemList
        itemMasterList.extend(inventory)
        for item in itemMasterList:
            # command should look like keyword + space + itemName: "use rope"
            for keywordAliasList in item.keywords.values():  # keywordAliasList = ('take', 'pick up')
                for kw in keywordAliasList:  # kw = 'take'
                    kw = kw.strip()
                    commandOnly = c.strip()  # commandOnly goes from 'take rope   ' to 'take rope'
                    # 'take' 'rope' / 'take rope'
                    #print(f'{kw} {item.name.strip()} / "{commandOnly}"')
                    #print(commandOnly == f"{kw} {item.name}")
                    if commandOnly == kw:  # if the user only said 'take' or 'use'
                        if not itemMsgGivenThisTurn:
                            display(f'{settings.ambiguousCmdMsg.replace("CMD_NAME", kw)}')
                            itemMsgGivenThisTurn = True
                        itemErrorMsgGiven = True
                    # 'take rope', 'turn on light', etc
                    elif commandOnly == f'{kw} {item.name}':
                        try:
                            itemMsgGivenThisTurn = True
                            if kw in item.keywords['use']:
                                if item in inventory:
                                    display(item.use())
                                    return True
                                else:
                                    display(settings.itemNotInInventoryMsg.replace('ITEM_NAME', item.name))
                                    return False
                            elif kw in item.keywords['take']:
                                takeItem(item.ID)
                                return True
                            elif kw in item.keywords['drop']:
                                dropItem(item.ID)
                                return True
                            else:
                                itemMsgGivenThisTurn = False
                                return False
                        except settings.ItemNotInInventoryException:
                            display(settings.itemNotInInventoryMsg.replace('ITEM_NAME', item.name))
                        except settings.invalidItemException:
                            display(settings.invalidItemMsg)
                            itemMsgGivenThisTurn = True
                            return False
                    else:
                        pass  # what do i do here?
        else:
            return False

    # checks to see if user tried to use a game command: looking around, checking inventory
    def gameCommandCheck(c):
        global invMsgGivenThisTurn
        if c in settings.lookAroundCmds:
            lookAround()
            return True
        elif c in settings.checkInvCmds:
            showInventory()
            invMsgGivenThisTurn = True
            return True
        else:
            return False

    # moves into the target room assuming dir is valid and all that. helper method for movementCommandCheck
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

    # checks to see if user tried to move
    def movementCommandCheck(dir):
        global roomList, currentRoom, currentRoomID, movedThisTurn, itemMsgGivenThisTurn
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
            if not itemMsgGivenThisTurn:
                display(settings.invalidCmdMsg)

    # ------- MAIN HIERARCHY ------- #
    lookedAroundThisTurn, itemMsgGivenThisTurn, invMsgGivenThisTurn = False, False, False
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

pygame.init()
# set up fonts here

# ------- MAIN GAME LOOP ------- #

crashed = False
while not crashed:
    pygame.display.flip()
    currentRoom = roomList[currentRoomID]
    # showItems(currentRoom)
    # showDestinations(currentRoom)
    # showInventory()
    if lookedAroundThisTurn or itemMsgGivenThisTurn or invMsgGivenThisTurn:
        nextInput = input('> ')
    elif movedThisTurn:
        nextInput = input(f'> {currentRoom.msgOnEnter}\n\n> ')
    else:
        nextInput = input(f'> {currentRoom.msgOnStay}\n\n> ')
    processCommand(nextInput.strip())


# ------- MAIN GAME LOOP ------- #
