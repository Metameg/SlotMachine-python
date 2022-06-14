import pygame
import random

class Symbol(object):
    def __init__(self, x, y, height, width, surface):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.isFalling = True
        self.fall_speed = 6
        self.surface = surface
        self.secret_number = random.randint(0, 2)
        self.images = [pygame.image.load("graphics/symbol_apple.png"),
                       pygame.image.load("graphics/symbol_orange.png"),
                       pygame.image.load("graphics/symbol_banana.png")]

    def draw_symbol(self):
        self.surface.blit(self.images[self.secret_number], (self.x, self.y))

    def fallTo(self, pledge):
        # Pledge is a int that is where you want to end up on the y coord
        if self.y < pledge:
            self.y += self.fall_speed
        else:
            self.isFalling = False


class MoneyButton(object):
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface
        self.balance = 0
        self.width = 60
        self.height = 30
        self.image = [pygame.image.load("graphics/money_button.png"), pygame.image.load("graphics/clicked_money_button.png")]
        self.jackpotImg = pygame.image.load("graphics/jackpot_button.png")
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mouse_pos = pygame.mouse.get_pos()
        

    def draw(self):
        self.surface.blit(self.image[0], (self.x, self.y))


    def isClicked(self):
        if self.rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.surface.blit(self.image[1], (self.x, self.y))
            self.surface.blit(self.image[1], (self.x + self.width + 20, self.y))
            return True
        else: 
            return False

    def drawJackpot(self):
        self.surface.blit(self.jackpotImg, (160, 15))


class SpinButton(object):
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface
        self.width = 60
        self.height = 30
        self.image = [pygame.image.load("graphics/spins_button.png"), pygame.image.load("graphics/clicked_spins_button.png")]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mouse_pos = pygame.mouse.get_pos()


    def draw(self):
        self.surface.blit(self.image[0], (self.x, self.y))


    def isClicked(self):
        if self.rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.surface.blit(self.image[1], (self.x, self.y))
            self.surface.blit(self.image[1], (self.x + self.width + 20, self.y))
        else:
            return None