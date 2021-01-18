import settings, pygame_input
from pygame import Rect
import pygame
import textwrap
from copy import deepcopy

pygame.display.init()


class TextArea:

    lineLimit = 5 # won't actually be 5, more like 19-20
    charLimit = 50  # chars per line
    verticalSpacing = 30  # px between lines
    margin = 30

    def __init__(self, dispSurface, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h  # x, y = top left corner
        self.centerX, centerY = x+w//2, y+h//2  # // = integer division
        self.lineLimit = (self.getMarginHeight() // 40) + 1
        self.text = '> '
        self.lines = []
        self.dispSurface = dispSurface

    def __repr__(self):
        return '\n'.join(self.lines)

    def addLines(self, *args):
        for line in args:
            self.lines.append(str(line))
            if len(self.lines) > self.lineLimit:
                self.text = self.text.replace(
                    self.lines[0], '', 1)  # 1 occurrence only
                self.lines.remove(self.lines[0])
        self.text = ''
        for line in self.lines:
            if str(line).strip().replace('>', '') == '':
                self.lines.remove(line)
            else:
                self.text += f'\n{str(line)}'

    def addText(self, text):  # a single string
        textToChange = deepcopy(text)
        if len(textToChange) > self.charLimit:
            textToChange = textwrap.fill(
                textToChange, width=self.charLimit).strip().replace('\n', '\n  ')
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
        pygame.event.clear()
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                    return text
                elif e.key == pygame.K_BACKSPACE:
                    if text.length > 0: text = text[:-1]
                elif pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
                    if e.key in settings.shiftMods:
                        text += settings.shiftMods[e.key]
                elif e.key in settings.alphanumericKeys.keys():
                    text += settings.alphanumericKeys[e.key]
            self.display()

        #when finished
        self.addText(text)
        return input(text)

    def getRect(self):
        return Rect(self.x, self.y, self.w, self.h)

    def getMarginRect(self):
        return Rect(self.x + self.margin, self.y + self.margin, self.w - 2*self.margin, self.h - 2*self.margin)

    def getMarginHeight(self):
        return self.h - 2*self.margin

    def shiftTextDown(self, numPixels): #animation
        pass
