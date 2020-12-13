roomNotFoundMsg = "Room not found. "
cannotMoveMsg = "Cannot move that direction. "
invalidDirMsg = "Not a valid direction. "

# USE TUPLES NOT LISTS HERE (saves memory)

possibleRoomNames = ("Library", "Kitchen", "Terrace", "Fountain", "Engine Room", "Garden", "Bedroom", "AP Office", "YSR Headquarters")

inputModes = (('North', 'north', 'N', 'n'), ('South', 'south', 'S', 's'), ('East', 'east', 'E', 'e'), ('West', 'west', 'W', 'w'))

#everything below this line is useless
# north = row-1, south = row+1, west = col-1, east = col+1
# should be added to a room's row and col
borderingTileVectors = ((-1, 0), (1, 0), (0, -1), (0, 1))
directionVectors = {
    "North": borderingTileVectors[0],
    "South": borderingTileVectors[1],
    "East": borderingTileVectors[2],
    "West": borderingTileVectors[3]
}

directionDict = { #why does this exist
    borderingTileVectors[0]: "North",
    borderingTileVectors[1]: "South",
    borderingTileVectors[2]: "East",
    borderingTileVectors[3]: "West"
}
