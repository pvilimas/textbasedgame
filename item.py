# not implemented at all
class Item:


    def __init__(self, name, keyword):
        self.name = name
        self.keyword = keyword
        self.msgOnUse = f'You used the {self.name}.'

    def __format__(self, format):
        return self.name

    def use(self):
        pass
