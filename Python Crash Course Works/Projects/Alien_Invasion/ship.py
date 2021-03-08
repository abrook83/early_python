import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ a class to manage the ship """

    def __init__(self, ai_game):        # references to itself and the current instance of the 'AlienInvasion Class'.
        """ initialise the ship and set its starting position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()     # allows us to place the ship in its current location

        # Load the ship's image and get its rectangle
        self.image = pygame.image.load('CrashProj/Projects/Alien_Invasion/freeship.bmp')     # load the image of the ship
        self.rect = self.image.get_rect()           # give the image the ship's location

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's position
        self.x = float(self.rect.x)
        
        # movement flags
        self.moving_right = False       # set 'False' initially
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag """
        # update the ship's x value, not the rect       
        if self.moving_right and self.rect.right < self.screen_rect.right:  # compares ship's position to screen size, cannpe exceed screen's x limit
            self.x += self.settings.ship_speed    # move right by increasing x value
        if self.moving_left and self.rect.left > 0:                                # setting 2 'if' statements removes either statement's priority
            self.x -= self.settings.ship_speed     # move left by decreasing x value
        
        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)