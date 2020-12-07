import item

class Room:

    msgOnEnter = "you have entered the " 
    msgOnStay = "you are in the "
    
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