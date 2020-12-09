roomNotFoundMsg = "Room not found. "
cannotMoveMsg = "Cannot move that direction. "
invalidDirMsg = "Not a valid direction. "

possibleRoomNames = ["Library", "Kitchen", "Terrace", "Fountain",
                     "Engine Room", "Garden", "Bedroom", "AP Office", "YSR Headquarters"]
# north = row-1, south = row+1, west = col-1, east = col+1
borderingTileVectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
directionVectors = {
    "North": borderingTileVectors[0],
    "South": borderingTileVectors[1],
    "East": borderingTileVectors[2],
    "West": borderingTileVectors[3]
}

directionDict = {
    borderingTileVectors[0]: "North",
    borderingTileVectors[1]: "South",
    borderingTileVectors[2]: "East",
    borderingTileVectors[3]: "West"
}
