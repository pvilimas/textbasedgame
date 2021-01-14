import pygame
import settings

def displayText(text):
    text = f'\n> {text}\n'
    return text

def customInput(text, type): #type = 'game' or 'user'
    return text