import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represent a singel alien in the fleet """

    def __init__(self, ai_game):
        """ initialise the alien and give it its starting location """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attributes
        self.image = pygame.image.load('Python Crash Course Works\Projects\Alien_Invasion/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)         # gives the alien's x position

    def check_edges(self):
        """ return True if alien is at the edge of screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """ move the alien to the left or right """
        self.x += (self.settings.alien_speed * 
                        self.settings.fleet_direction)         # move alien by incrementing at each refresh at the speed in settings.py
        self.rect.x = self.x                # update position of the alien's rectangle


