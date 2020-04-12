import pygame
import sys
from setting import Setting
from ship import Ship
import game_function as gf

def run_game():
    #initiliza the game and create an object
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))

    bg_color = (230, 230, 230)
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_setting,screen)

    #start the game loop
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting,screen,ship)

        #monitor the keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



            #reconstruct image every time the game started
            screen.fill(ai_setting.bg_color)
            ship.blitme()

            #make the image visible
            pygame.display.flip()











run_game()