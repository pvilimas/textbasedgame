import item


class Room:

    #later on, set self.roomNotFoundMsg to be the stuff from settings and then manually change it for certain rooms (text overrides)
    #also maybe override the two methods below

    msgOnEnter = "You have entered the "
    msgOnStay = "You are in the "

    def __init__(self, name, ID, itemList):
        self.name = name
        self.ID = ID
        self.itemList = itemList
        self.msgOnEnter += name
        self.msgOnStay += name
        self.destinations = {
            "North": None,
            "South": None,
            "East": None,
            "West": None
        }

    # format method
    def __format__(self, format):
        if (format == 'short'):
            return '{} [{}] | '.format(self.name.ljust(18, ' '), self.ID)
        if (format == 'shorter'):
            return '{}'.format(self.name).ljust(18, ' ')
        return '{} [{}]: {d} | '.format(self.name.ljust(18, ' '), self.ID, d=' '.join(str(x).ljust(4, ' ') for x in self.destinations.values()))
