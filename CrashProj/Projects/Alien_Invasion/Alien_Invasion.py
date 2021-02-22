import sys          # import both the 'sys' and 'pygame' modules
                    # sys allows us to access system-specific modules & functions (like to Quit the game)
import pygame       # pygame contains the functionality to make a game.

from settings import Settings       # game settings are in the settings.py file....
from ship import Ship               # import the image and attributes of the ship
from bullet import Bullet           # import the bullets for Bullet

class AlienInvasion:
    """ Overall class to manage game assets and behaviour """ 

    def __init__(self):
        """ initialise the game and create game resources """

        pygame.init()       # initialises the background settings to allow pygame to run
        self.settings = Settings()      # assigns an instance of 'Settings' from the class in settings.py, assign to self.settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))      # creates a display window from settings
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)      # make an instance of the ship after the screen has been created
        self.bullets = pygame.sprite.Group()

        # set the background colour
        self.bg_colour = (0, 95, 135)

    def run_game(self):                     # the game runs by this method
        """ Start the main loop for the game """
        while True:                         # continuous loop
            self._check_events()        # runs the '_check_events' method
            self.ship.update()          # updates ship's position after checking for keyboard events
            self._update_bullets()
            self._update_screen()       # runs the '_update_screen' method

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():        # an event loop, returns a list of events that have taken place since the... 
            if event.type == pygame.QUIT:       # last iteration of the loop. Runs at every mouse or keyboard event.
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:           # sets movement to 'False' as the key is released. Allows for continuous movement.
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """ respond to keypresses """
        if event.key == pygame.K_RIGHT:   # moves the ship to the right when right key pressed
            self.ship.moving_right = True       # calls the 'moving_right' function from the update method in Ship class
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:       # assign the SPACEBAR to the 'fire bullets' method
            self._fire_bullet()
        

    def _check_keyup_events(self, event):
        """ respond to key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ create a new bullet and add it to the new bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:        # limits the number of bullets to the number in settings.py
            new_bullet = Bullet(self)           # make an instance of a bullet from the class and...
            self.bullets.add(new_bullet)        # add it to the list of bullets
    
    def _update_bullets(self):
        """ update position of bullets and get rid of old bullets """
        # update bullet positions
        self.bullets.update()       # calls bullet.update() for each in the group of bullets
 
        # get rid of bullets that have reached the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)          
    
    def _update_screen(self):
        # updates images on the screen, and flip to a new screen
        # redraw the screen with each pass of the loop
        self.screen.fill(self.bg_colour)        # with settings imported from Settings class
        self.ship.blitme()          # draw the ship on the screen, on top of the background
        for bullet in self.bullets.sprites():       # returns a list of all the bullets...
            bullet.draw_bullet()                    # call 'draw bullet' in bullet.py

        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


