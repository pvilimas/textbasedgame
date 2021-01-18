import settings
import pygame

pygame.display.init()

def displayText(text):
    text = f'\n> {text}\n'
    return text

def displayInput(text, type): #type = 'game' or 'user'
    return text

class TextArea:

    numLines = 5
    def __init__(self, dispSurface):
        self.text = ''
        self.lines = []
        self.dispSurface = dispSurface
    
    def __repr__(self):
        return '\n'.join(self.lines)

    def addLines(self, *args):
        for line in args:
            self.lines.append(str(line))
            self.text += f'\n{str(line)}'

    def display(self):
        txt = settings.gameFont.render(self.text, True, settings.gameColor)
        self.dispSurface.blit(txt, (400, 400))