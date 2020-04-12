import sys
import pygame

def check_keydown_events(event,ship):
    """respond key-pressing"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    """respond losing key-pressing"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """respond to mouse and keyboard"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def update_screen(ai_setting,screen,ship):
    """update image and replace with new screen"""
    #recreate image every loop
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    #make new image visible
    pygame.display.flip()
