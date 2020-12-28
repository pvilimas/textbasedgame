# not implemented at all
# hi it is omar
class Item:


    def __init__(self, name, keyword):
        self.name = name
        self.keyword = keyword

        self.msgOnUse = f'You used the {self.name}.'

    def __format__(self, format):
        return self.name

    def use(self):
        pass
