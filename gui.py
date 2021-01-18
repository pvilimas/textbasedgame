import settings
from pygame import Rect
import pygame
import textwrap
from copy import deepcopy

pygame.display.init()


def displayText(text):
    text = f'\n> {text}\n'
    return text


def displayInput(text, type):  # type = 'game' or 'user'
    return text


class TextArea:

    lineLimit = 5
    charLimit = 50  # per line
    verticalSpacing = 30  # px
    margin = 30

    def __init__(self, dispSurface, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h  # x, y = top left corner
        self.centerX, centerY = x+w//2, y+h//2  # // = integer division
        self.lineLimit = (self.getMarginHeight() // 40) + 1
        print(self.lineLimit)
        self.text = ''
        self.lines = []
        self.dispSurface = dispSurface

    def __repr__(self):
        return '\n'.join(self.lines)

    def addLines(self, *args):
        for line in args:
            self.lines.append(str(line))
            if len(self.lines) > self.lineLimit:
                self.text = self.text.replace(self.lines[0], '', 1)
                self.lines.remove(self.lines[0])
            self.text += f'\n{str(line)}'

    def addText(self, text):  # a single string
        textToChange = deepcopy(text)
        if len(textToChange) > self.charLimit:
            textToChange = textwrap.fill(textToChange, width=self.charLimit).strip()
        for lineToAdd in textToChange.split('\n'):
            self.addLines(lineToAdd)

    def display(self):
        pygame.draw.rect(self.dispSurface,
                             settings.medGray, self.getRect(), 3)
        #pygame.draw.rect(self.dispSurface, settings.red, self.getMarginRect(), 3)
        for i, line in enumerate(self.lines):
            txt = settings.gameFont.render(line, True, settings.gameTextColor)
            pygame.draw.rect(self.dispSurface,
                             settings.medGray, self.getRect(), 3)
            # print(self.getMarginHeight())
            self.dispSurface.blit(
                txt, (self.x+self.margin, self.y + self.margin + (i*self.verticalSpacing)))

    def customInput(self, text):
        self.addText(text)
        return input(text)

    def getRect(self):
        return Rect(self.x, self.y, self.w, self.h)

    def getMarginRect(self):
        return Rect(self.x + self.margin, self.y + self.margin, self.w - 2*self.margin, self.h - 2*self.margin)

    def getMarginHeight(self):
        return self.h - 2*self.margin

    def shiftTextDown(self, numPixels):
        pass
