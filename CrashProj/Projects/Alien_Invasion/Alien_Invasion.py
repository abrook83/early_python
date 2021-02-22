import sys          # import both the 'sys' and 'pygame' modules
                    # sys allows us to access system-specific modules & functions (like to Quit the game)
import pygame       # pygame contains the functionality to make a game.

from settings import Settings       # game settings are in the settings.py file....
from ship import Ship               # import the image and attributes of the ship

class AlienInvasion:
    """ Overall class to manage game assets and behaviour """ 

    def __init__(self):
        """ initialise the game and create game resources """

        pygame.init()       # initialises the background settings to allow pygame to run
        self.settings = Settings()      # assigns an instance of 'Settings' from the class in settings.py, assign to self.settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))      # creates a display window from settings
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)      # make an instance of the ship after the screen has been created

        # set the background colour
        self.bg_colour = (0, 95, 135)

    def run_game(self):                     # the game runs by this method
        """ Start the main loop for the game """
        while True:                         # continuous loop
            # Watch for keyboard and mouse events
            for event in pygame.event.get():        # an event loop, returns a list of events that have taken place since the 
                if event.type == pygame.QUIT:       # last iteration of the loop. Runs at every mouse or keyboard event.
                    sys.exit()

            # redraw the screen with each pass of the loop
            self.screen.fill(self.bg_colour)        # with settings imported from Settings class
            self.ship.blitme()          # draw the ship on the screen, on top of the background

            # Make the most recently drawn screen visible
            pygame.display.flip()         

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


