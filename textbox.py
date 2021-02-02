from ursina import *
from textwrap import wrap
import settings


class TextBox():
    def __init__(self, x, y, startingText='', height=13, width=80):
        self.x = x
        self.y = y
        self.text = startingText
        self.height = height
        self.width = width
        self.lines = ['']  # List[str]

    def addLine(self, line):
        self.lines.append(line.rstrip())
    
    def addLines(self, lines):
        for l in lines:
            self.addLine(l)
    
    def addText(self, text):
        self.addLines(wrap(text, width=self.width))
    
    def removeChar(self): #used for backspacing
        if len(self.lines[-1]) > 0:
             self.lines[-1] = self.lines[-1][:-1]

    def addChar(self, char):
        if len(self.lines[-1]) <= self.width:
            self.lines[-1] += char

    def getTextField(self):
        pass

    def getFormattedText(self):
        return '\n'.join([f'> {line}' for line in self.lines])
    
    def __repr__(self, format=''):
        return self.getFormattedText().strip() + " formatted tb"

    def display(self, text=''):
        if text == '':
            text = self.text
            print(repr(self))