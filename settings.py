roomNotFoundMsg = "Room not found. "  # currently unused
# displayed when a player tries to move north when there's no room that way
invalidDirMsg = "Not a valid direction. "
# displayed when a player tries to move sdmcnsbnd or use the 23846sajbd
invalidCmdMsg = "Command not recognized. "

# USE TUPLES NOT LISTS HERE (saves memory)

possibleRoomNames = ("Library", "Kitchen", "Terrace", "Fountain",
                     "Engine Room", "Garden", "Bedroom", "AP Office", "YSR Headquarters", "Hoe Hackett Shack")
inputModes = (('North', 'north', 'N', 'n'), ('South', 'south', 'S', 's'), ('East', 'east', 'E', 'e'), ('West', 'west', 'W', 'w'),
              ('Northeast', 'northeast', 'NE', 'ne'), ('Southeast', 'southeast', 'SE', 'se'), ('Northwest', 'northwest', 'NW', 'nw'), ('Southwest', 'southwest', 'SW', 'sw'))

# this only exists for showDestinations purposes              
abbrDirections = dict()
for i in inputModes:
    abbrDirections.update({i[0]: i[2]})

# these are the only ones the move method can handle
validDirections = (dirList[0] for dirList in inputModes)

lookAroundCmds = ("look", "look around", "Look", "Look around", "Look Around")
