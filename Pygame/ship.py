import pygame

class Ship():

    def __init__(self,ai_setting,screen):
        """init ship to original spot"""
        self.screen = screen
        self.ai_setting = ai_setting

         #load image and put into a rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

         #put every new ship in the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store number in center
        self.center = float(self.rect.centerx)

        # moving sign
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """based on the moving sigh to move the ship"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center



    def blitme(self):
        """create ship in the given spot"""
        self.screen.blit(self.image, self.rect)






