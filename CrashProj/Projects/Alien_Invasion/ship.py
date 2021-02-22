import pygame

class Ship:
    """ a class to manage the ship """

    def __init__(self, ai_game):        # references to itself and the current instance of the 'AlienInvasion Class'.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()     # allows us to place the ship in its current location

        # Load the ship's image and get its rectangle
        self.image = pygame.image.load('CrashProj/Projects/Alien_Invasion/freeship.bmp')     # load the image of the ship
        self.rect = self.image.get_rect()           # give the image the ship's location

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

