# not implemented at all
class Item:


    def __init__(self, name, kwUse): #kwUse MUST BE A TUPLE OR A LIST
        self.name = name
        self.keywords = {
            'use': kwUse,
            'pickup': ['pick up'],
            'drop': ['drop']
        }
        self.msgOnUse = f'You used the {self.name}.'

    def __format__(self, format):
        return self.name

    def use(self):
        pass
