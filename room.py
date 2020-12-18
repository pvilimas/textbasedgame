import item
import settings


class Room:

    # all of these should be customized in initializeManual later
    msgOnEnter = "You have entered the "  # upon entering
    msgOnLook = "You are in the "
    msgOnStay = "You are in the "  # after a failed attempt at moving

    # error messages, can be customized in initializeManual
    roomNotFoundMsg = settings.roomNotFoundMsg
    cannotMoveMsg = settings.cannotMoveMsg
    invalidDirMsg = settings.invalidDirMsg

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.itemList = []
        self.msgOnEnter = f'You have entered the {self.name}'
        self.msgOnLook = f'You are in the {self.name}'
        self.msgOnStay = f'You are in the {self.name}'
        self.destinations = dict()
        for d in settings.validDirections:
            self.destinations.update({d: None})

    # format method

    def __format__(self, format):
        if (format == 'short'):
            return '{} [{}] | '.format(self.name.ljust(18, ' '), self.ID)
        if (format == 'shorter'):
            return '{}'.format(self.name).ljust(18, ' ')
        return '{} [{}]: {d} | '.format(self.name.ljust(18, ' '), self.ID, d=' '.join(str(x).ljust(4, ' ') for x in self.destinations.values()))
