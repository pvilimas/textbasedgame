class Item:


    def __init__(self, name, ID, kwUse): #kwUse MUST BE A TUPLE OR A LIST
        self.name = name
        self.ID = ID
        self.keywords = {
            'use': kwUse,
            'pickup': ['pick up'],
            'drop': ['drop']
        }
        self.msgOnUse = f'You used the {self.name}.'
        self.canBePickedUp = True #must be set to false manually in initializeManual

    def __format__(self, format):
        return self.name

    def use(self):
        pass
