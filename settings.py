# currently unused
roomNotFoundMsg = 'Room not found. ' 
# displayed when a player tries to move north when there's no room that way
invalidDirMsg = 'You can\'t go that way! '
# displayed when a player tries to move sdmcnsbnd or use the 23846sajbd
invalidCmdMsg = 'Command not recognized! '
# displayed when a player tries to interact with an item that doesn't exist
invalidItemMsg = 'That item doesn\'t exist! '
# displayed when a player says "take" or "use" with no object in the command
ambiguousCmdMsg = 'Specify an object.'  # 'take?'
# displayed when an item is not found in the inventory
itemNotInInventoryMsg = 'That couldn\'t be found in your inventory!'
# displayed when an item is not found in the room
itemNotInRoomMsg = 'You couldn\'t find that item anywhere here. '
# displayed when an item is mentioned without any action
unknownItemActionMsg = 'What do you want to do with the ITEM_NAME?'


# USE TUPLES NOT LISTS HERE (saves memory)

possibleRoomNames = ('Library', 'Kitchen', 'Terrace', 'Fountain',
                     'Engine Room', 'Garden', 'Bedroom', 'AP Office', 'YSR Headquarters', 'Hoe Hackett Shack')
possibleItemNames = ('rope', 'computer', 'plunger',
                     'daddy kehne head polish', 'apple')
# MAKE SURE THIS IS UPDATED
pluralItemNames = ('rope', 'daddy kehne head polish', 'computers', 'apples', 'plungers')
inputModes = (('North', 'north', 'N', 'n'), ('South', 'south', 'S', 's'), ('East', 'east', 'E', 'e'), ('West', 'west', 'W', 'w'),
              ('Northeast', 'northeast', 'NE', 'ne'), ('Southeast', 'southeast', 'SE', 'se'), ('Northwest', 'northwest', 'NW', 'nw'), ('Southwest', 'southwest', 'SW', 'sw'))

# this only exists for showDestinations purposes - Northwest: NW
abbrDirections = dict()
for i in inputModes:
    abbrDirections.update({i[0]: i[2]})

# these are the only ones the move method can handle
validDirections = (dirList[0] for dirList in inputModes)

lookAroundCmds = ('look', 'look around', 'Look', 'Look around',
                  'Look Around')  # hmm i wonder what these do
# commands to look through the inventory
checkInvCmds = ('inventory', 'Inventory', 'inv', 'Inv')

class CannotTakeItemException(Exception):
    pass


class ItemNotInInventoryException(Exception):
    pass
class invalidItemException(Exception):
    pass