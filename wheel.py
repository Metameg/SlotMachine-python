import pygame
import symbols

# Constants
DISPLAYWIDTH = 500
DISPLAYHEIGHT = 500
DISPLAY = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))

class wheel(object): 
    slot_one = symbols.Symbol(225, 215, 64, 64, DISPLAY)
    slot_two = symbols.Symbol(225, 215, 64, 64, DISPLAY)
    slot_three = symbols.Symbol(225, 215, 64, 64, DISPLAY)
    slot_dummy = symbols.Symbol(225, 215, 64, 64, DISPLAY)

    def __init__(self, x, y, height, width, surface):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.isFalling = True
        self.fall_speed = 6
        self.surface = surface
        
        self.images = [pygame.image.load("graphics/symbol_apple.png"),
                       pygame.image.load("graphics/symbol_orange.png"),
                       pygame.image.load("graphics/symbol_banana.png")]