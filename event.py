import item
import settings

class Event:
    #contextual action that occurs in certain rooms
    def __init__(self, name, ID, kwUsable, kwInteract, msgOnInteract):
        self.name = name
        self.ID = ID
        self.keywords = {
            'interact': kwInteract,
            'usable': kwUsable,
            'touch': {'touch', 'feel'},
        }
        self.msgOnInteract = msgOnInteract
    
    

            