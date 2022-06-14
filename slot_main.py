import pygame
from pygame.constants import MOUSEBUTTONDOWN
import symbols
#import player

# Constants
DISPLAYWIDTH = 500
DISPLAYHEIGHT = 500
DISPLAY = pygame.display.set_mode((DISPLAYWIDTH,DISPLAYHEIGHT))
BUTTON_RECT = pygame.Rect(400, 100, 100, 100)
FINAL_MACHINE = pygame.image.load("graphics/slot_eleven.png")


# Variables
clock = pygame.time.Clock()
FPS = 50
count = 0
play_again = False
run = True
backgroundList = [pygame.image.load("graphics/slot_one.png"),
                  pygame.image.load("graphics/slot_two.png"),
                  pygame.image.load("graphics/slot_three.png"),
                  pygame.image.load("graphics/slot_four.png"),
                  pygame.image.load("graphics/slot_five.png"),
                  pygame.image.load("graphics/slot_six.png"),
                  pygame.image.load("graphics/slot_seven.png"),
                  pygame.image.load("graphics/slot_eight.png"),
                  pygame.image.load("graphics/slot_nine.png"),
                  pygame.image.load("graphics/slot_ten.png"),
                  pygame.image.load("graphics/slot_eleven.png")]

# Instances
slot_one = symbols.Symbol(225, 215, 64, 64, DISPLAY)
slot_two = symbols.Symbol(225, 215, 64, 64, DISPLAY)
slot_three = symbols.Symbol(225, 215, 64, 64, DISPLAY)
slot_dummy = symbols.Symbol(225, 215, 64, 64, DISPLAY)

money_button = symbols.MoneyButton(25, 25, DISPLAY)
spins_button = symbols.SpinButton(25, 75, DISPLAY)
lever_pulled = False
initial_screen = True
frame_count = 0
start_time = 0
spin_count = 0

pygame.init()
pygame.display.set_caption("Click the Button")


def spin_wheel():
    
    global spin_count
    global slot_dummy

    NUMBER_OF_DUMMY_SPINS = 5
    
    slot_dummy.fall_speed = 30
    slot_dummy.draw_symbol()
    slot_dummy.fallTo(440)
    DISPLAY.blit(FINAL_MACHINE, (0,0))

    if (slot_dummy.isFalling == False) and (spin_count < NUMBER_OF_DUMMY_SPINS):
        slot_dummy = symbols.Symbol(225, 215, 64, 64, DISPLAY)
        spin_count += 1
        
    if spin_count == NUMBER_OF_DUMMY_SPINS and slot_dummy.isFalling == False:
        finish_spin()


def finish_spin():
    slot_one.draw_symbol()
    slot_one.fallTo(365)
    if not slot_one.isFalling:
        slot_two.draw_symbol()
        slot_two.fallTo(290)
    if not slot_two.isFalling:
        slot_three.draw_symbol()
        slot_three.fallTo(220)
    
def pull_lever():
    global frame_count

    while frame_count <= 50:
        frame_count += 1
        DISPLAY.blit(backgroundList[frame_count // 5], (0,0))
        pygame.display.update()
    
    DISPLAY.blit(FINAL_MACHINE, (0,0))
    
def check_win():
    if slot_one.secret_number == slot_two.secret_number == slot_three.secret_number:
        money_button.drawJackpot()





while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        collide = BUTTON_RECT.collidepoint(mouse_pos)
        if event.type == pygame.QUIT:
            run = False
        if collide and event.type == MOUSEBUTTONDOWN:
            lever_pulled = True
                
    DISPLAY.fill("white")

    if lever_pulled:
        start_time = pygame.time.get_ticks()
       
        #pull_lever()
        
        spin_wheel()
        
        
            

        if not slot_three.isFalling:
            lever_pulled = False
        
        initial_screen = False
        

    elif not lever_pulled and not initial_screen:
        slot_one.draw_symbol()
        slot_two.draw_symbol()
        slot_three.draw_symbol()
        DISPLAY.blit(FINAL_MACHINE,(0,0))
       
        check_win()

        if money_button.isClicked():
            # re-initialize all variables back to initial_screen
            lever_pulled = False
            initial_screen = True
            frame_count = 0
            slot_one = symbols.Symbol(225, 215, 64, 64, DISPLAY)
            slot_two = symbols.Symbol(225, 215, 64, 64, DISPLAY)
            slot_three = symbols.Symbol(225, 215, 64, 64, DISPLAY)
            slot_dummy = symbols.Symbol(225, 215, 64, 64, DISPLAY)
            spin_count = 0
            
            
    else:
        DISPLAY.blit(backgroundList[0],(0,0))

    # DRAW Buttons
    money_button.draw()
    money_button.mouse_pos = pygame.mouse.get_pos()
    money_button.isClicked()
    spins_button.draw()
    spins_button.mouse_pos = pygame.mouse.get_pos()
    spins_button.isClicked()
    

    pygame.display.update()
pygame.quit()