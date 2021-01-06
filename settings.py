roomNotFoundMsg = "Room not found. "  # currently unused
# displayed when a player tries to move west but there is no room west of here
cannotMoveMsg = "Cannot move that direction. "
# displayed when a player tries to move "msdkaasjbhdjh" instead of "north" or "W"
invalidDirMsg = "Not a valid direction. "

# USE TUPLES NOT LISTS HERE (saves memory)

possibleRoomNames = ("Library", "Kitchen", "Terrace", "Fountain",
                     "Engine Room", "Garden", "Bedroom", "AP Office", "YSR Headquarters", "Hoe Hackett Shack")
inputModes = (('North', 'north', 'N', 'n'), ('South', 'south', 'S', 's'), ('East', 'east', 'E', 'e'), ('West', 'west', 'W', 'w'),
              ('Northeast', 'northeast', 'NE', 'ne'), ('Southeast', 'southeast', 'SE', 'se'), ('Northwest', 'northwest', 'NW', 'nw'), ('Southwest', 'southwest', 'SW', 'sw'))

# these are the only ones the move method can handle
validDirections = (dirList[0] for dirList in inputModes)

lookAroundCmds = ("look", "look around", "Look", "Look around", "Look Around")
