import pygame
roomNotFoundMsg = 'Room not found. '  # currently unused
# displayed when a player tries to move north when there's no room that way
invalidDirMsg = 'You can\'t go that way! '
# displayed when a player tries to move sdmcnsbnd or use the 23846sajbd
invalidCmdMsg = 'Command not recognized! '
# displayed when a player tries to interact with an item that doesn't exist
invalidItemMsg = 'That item doesn\'t exist! '
# displayed when a player says "take" or "use" with no object in the command
ambiguousCmdMsg = 'What do you want to CMD_NAME? '
# displayed when an item is not found in the inventory
itemNotInInventoryMsg = 'No ITEM_NAME was found in your inventory! '

# USE TUPLES NOT LISTS HERE (saves memory)

possibleRoomNames = ('Library', 'Kitchen', 'Terrace', 'Fountain',
                     'Engine Room', 'Garden', 'Bedroom', 'AP Office', 'YSR Headquarters', 'Hoe Hackett Shack')
possibleItemNames = ('rope', 'computer', 'plunger',
                     'daddy kehne head polish', 'apple')
# MAKE SURE THIS IS UPDATED
pluralItemNames = ('rope', 'daddy kehne head polish')
inputModes = (('North', 'north', 'N', 'n'), ('South', 'south', 'S', 's'), ('East', 'east', 'E', 'e'), ('West', 'west', 'W', 'w'),
              ('Northeast', 'northeast', 'NE', 'ne'), ('Southeast', 'southeast', 'SE', 'se'), ('Northwest', 'northwest', 'NW', 'nw'), ('Southwest', 'southwest', 'SW', 'sw'))

# this only exists for showDestinations purposes - Northwest: NW
abbrDirections = dict()
for i in inputModes:
    abbrDirections.update({i[0]: i[2]})

# these are the only ones the move method can handle
validDirections = (dirList[0] for dirList in inputModes)

lookAroundCmds = ('look', 'look around', 'Look', 'Look around',
                  'Look Around')  # hmm i wonder what these do
# commands to look through the inventory
checkInvCmds = ('inventory', 'Inventory', 'inv', 'Inv')

# GUI stuff
pygame.init()
dispHeight = 800
dispWidth = 800
gameFPS = 30

white = (255, 255, 255)
green = (10, 128, 43)
darkGray = (40, 40, 40)
medGray = (50, 50, 50)
red = (230, 20, 20)

bgColor = darkGray
gameTextColor = green
userTextColor = green  # for now
gameFont = pygame.font.Font('data//fonts//AndaleMono.ttf', 20)

# used for customInput in TextArea class
alphanumericKeys = {
    pygame.K_SPACE: ' ',
    pygame.K_EXCLAIM: '!',
    pygame.K_QUOTEDBL: '"',
    pygame.K_HASH: '#',
    pygame.K_DOLLAR: '$',
    pygame.K_AMPERSAND: '&',
    pygame.K_QUOTE: " '",
    pygame.K_LEFTPAREN: '(',
    pygame.K_RIGHTPAREN: ')',
    pygame.K_ASTERISK: '*',
    pygame.K_PLUS: '+',
    pygame.K_COMMA: ',',
    pygame.K_MINUS: '-',
    pygame.K_PERIOD: '.',
    pygame.K_SLASH: '/',
    pygame.K_0: '0',
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_9: '9',
    pygame.K_COLON: ':',
    pygame.K_SEMICOLON: ';',
    pygame.K_LESS: '<',
    pygame.K_EQUALS: '=',
    pygame.K_GREATER: '>',
    pygame.K_QUESTION: '?',
    pygame.K_AT: '@',
    pygame.K_LEFTBRACKET: '[',
    pygame.K_BACKSLASH: '\\',
    pygame.K_RIGHTBRACKET: ']',
    pygame.K_CARET: '^',
    pygame.K_UNDERSCORE: '_',
    pygame.K_BACKQUOTE: '`',
    pygame.K_a: 'a',
    pygame.K_b: 'b',
    pygame.K_c: 'c',
    pygame.K_d: 'd',
    pygame.K_e: 'e',
    pygame.K_f: 'f',
    pygame.K_g: 'g',
    pygame.K_h: 'h',
    pygame.K_i: 'i',
    pygame.K_j: 'j',
    pygame.K_k: 'k',
    pygame.K_l: 'l',
    pygame.K_m: 'm',
    pygame.K_n: 'n',
    pygame.K_o: 'o',
    pygame.K_p: 'p',
    pygame.K_q: 'q',
    pygame.K_r: 'r',
    pygame.K_s: 's',
    pygame.K_t: 't',
    pygame.K_u: 'u',
    pygame.K_v: 'v',
    pygame.K_w: 'w',
    pygame.K_x: 'x',
    pygame.K_y: 'y',
    pygame.K_z: 'z',
    pygame.K_KP0: '0',
    pygame.K_KP1: '1',
    pygame.K_KP2: '2',
    pygame.K_KP3: '3',
    pygame.K_KP4: '4',
    pygame.K_KP5: '5',
    pygame.K_KP6: '6',
    pygame.K_KP7: '7',
    pygame.K_KP8: '8',
    pygame.K_KP9: '9',
    pygame.K_KP_PERIOD: '.',
    pygame.K_KP_DIVIDE: '/',
    pygame.K_KP_MULTIPLY: '*',
    pygame.K_KP_MINUS: '-',
    pygame.K_KP_PLUS: '+',
    pygame.K_KP_EQUALS: '='
}

shiftMods = {
    pygame.K_a: 'a'.upper(),
    pygame.K_b: 'b'.upper(),
    pygame.K_c: 'c'.upper(),
    pygame.K_d: 'd'.upper(),
    pygame.K_e: 'e'.upper(),
    pygame.K_f: 'f'.upper(),
    pygame.K_g: 'g'.upper(),
    pygame.K_h: 'h'.upper(),
    pygame.K_i: 'i'.upper(),
    pygame.K_j: 'j'.upper(),
    pygame.K_k: 'k'.upper(),
    pygame.K_l: 'l'.upper(),
    pygame.K_m: 'm'.upper(),
    pygame.K_n: 'n'.upper(),
    pygame.K_o: 'o'.upper(),
    pygame.K_p: 'p'.upper(),
    pygame.K_q: 'q'.upper(),
    pygame.K_r: 'r'.upper(),
    pygame.K_s: 's'.upper(),
    pygame.K_t: 't'.upper(),
    pygame.K_u: 'u'.upper(),
    pygame.K_v: 'v'.upper(),
    pygame.K_w: 'w'.upper(),
    pygame.K_x: 'x'.upper(),
    pygame.K_y: 'y'.upper(),
    pygame.K_z: 'z'.upper(),
    pygame.K_0: ')',
    pygame.K_1: '!',
    pygame.K_2: '@',
    pygame.K_3: '#',
    pygame.K_4: '$',
    pygame.K_5: '%',
    pygame.K_6: '^',
    pygame.K_7: '&',
    pygame.K_8: '*',
    pygame.K_9: '(',
    pygame.K_KP0: ')',
    pygame.K_KP1: '!',
    pygame.K_KP2: '@',
    pygame.K_KP3: '#',
    pygame.K_KP4: '$',
    pygame.K_KP5: '%',
    pygame.K_KP6: '^',
    pygame.K_KP7: '&',
    pygame.K_KP8: '*',
    pygame.K_KP9: '(',
}

class CannotTakeItemException(Exception):
    pass


class ItemNotInInventoryException(Exception):
    pass


class invalidItemException(Exception):
    pass
