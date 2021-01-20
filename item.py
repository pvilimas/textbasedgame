import settings


class Item:

    def __init__(self, name, ID, kwUse):  # kwUse MUST BE A TUPLE (list not recommended)
        self.name = name
        self.ID = ID
        self.keywords = {
            'use': kwUse,
            'take': ('take', 'pick up', 'grab'),
            'drop': ('drop', 'put down')
        }
        self.msgOnUse = f'You used the {self.name}. '
        self.msgOnTake = f'You took the {self.name}. '
        self.msgOnDrop = f'You dropped the {self.name}. '
        self.msgOnLook = f'This is just a regular {self.name}. ' #not implemented yet
        self.canBePickedUp = True  # must be set to false manually in initializeManual

    def __format__(self, format):
        if self.name in settings.pluralItemNames:
            return f'some {self.name}'
        else:
            return f'an {self.name}' if self.name[0] in 'aeiou' else f'a {self.name}'

    def __repr__(self):
        return self.__format__(self)

    def use(self):  # must be called like: display(item.use())
        return self.msgOnUse  # do not remove this
