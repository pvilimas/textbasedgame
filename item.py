class Item:


    def __init__(self, name, ID, kwUse): #kwUse MUST BE A TUPLE OR A LIST
        self.name = name
        self.ID = ID
        self.keywords = {
            'use': kwUse,
            'pick up': ['pick up'],
            'drop': ['drop']
        }
        self.msgOnUse = f'You used the {self.name}.'
        self.canBePickedUp = True #must be set to false manually in initializeManual

    def __format__(self, format):
        if self.name == 'rope': return f'some {self.name}' #add more conditions here
        else: return f'an {self.name}' if self.name[0] in 'aeiou' else f'a {self.name}'

    def __repr__(self):
        return self.__format__(self)

    def use(self):
        pass
