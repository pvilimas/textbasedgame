from ursina import *
import settings

class CustomInputField(InputField):
    def __init__(self, **kwargs): #just use font, font_size, max_lines=13
        super().__init__(**kwargs)