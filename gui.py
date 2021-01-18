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
    verticalSpacing = 30 # px
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
    
    def addText(self, text): # a single string
        for lineToAdd in text.split('\n'):
            self.addLines(lineToAdd)

    def display(self):
        for i, line in enumerate(self.lines):
            txt = settings.gameFont.render(line, True, settings.gameTextColor)
            self.dispSurface.blit(txt, (400, 400 + (i*self.verticalSpacing)))