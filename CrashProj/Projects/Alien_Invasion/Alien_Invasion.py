import sys          # import both the 'sys' and 'pygame' modules
from time import sleep
                    # sys allows us to access system-specific modules & functions (like to Quit the game)
import pygame       # pygame contains the functionality to make a game.

from settings import Settings       # game settings are in the settings.py file....
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship               # import the image and attributes of the ship
from bullet import Bullet           # import the bullets for Bullet
from alien import Alien             


class AlienInvasion:
    """ Overall class to manage game assets and behaviour """ 

    def __init__(self):
        """ initialise the game and create game resources """
        pygame.init()       # initialises the background settings to allow pygame to run
        self.settings = Settings()      # assigns an instance of 'Settings' from the class in settings.py, assign to self.settings
 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # create an instance to store the game's stats & create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)      # make an instance of the ship after the screen has been created
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()        # create a group to hold the aliens

        # Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):                     # the game runs by this method
        """ Start the main loop for the game """
        while True:                         # continuous loop
            self._check_events()        # runs the '_check_events' method
            
            if self.stats.game_active:
                self.ship.update()          # updates ship's position after checking for keyboard events
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()       # runs the '_update_screen' method

    def _check_events(self):
        """ Watch for keyboard and mouse events """
        for event in pygame.event.get():        # an event loop, returns a list of events that have taken place since the... 
            if event.type == pygame.QUIT:       # last iteration of the loop. Runs at every mouse or keyboard event.
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:           # sets movement to 'False' as the key is released. Allows for continuous movement.
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
            """ start a new game when player clicks 'Play' button """
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.stats.game_active:
                # reset the game settings
                self.settings.initialise_dynamic_settings()
                self.stats.reset_stats()
                self.stats.game_active = True
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_ships()
                # hide the mouse cursor
                pygame.mouse.set_visible(False)

            # get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet
            self.ship.center_ship()

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ respond to bullet alien collisions """
        # remove any bullets and aliens that collide
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()  

        if not self.aliens:
            # destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """ check if the fleet is at an adge,
        and update positions of all aliens in the fleet """
        self._check_fleet_edges()
        self.aliens.update()

        # look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()      

    def _check_aliens_bottom(self):
        """ check if the aliens have reached the bottom of the screen """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if the ship was hit
                self._ship_hit()
                break

    def _ship_hit(self):
        """ respond to the ship being hit by an alien """
        if self.stats.ships_left > 0:
            # decrement ships left, & update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # get gid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """ create the fleet of aliens """
        # create an alien and find the number of aliens in a row
        # spacing between aliens is equal to the width of one alien
        alien = Alien(self)                         # create an alien
        alien_width, alien_height = alien.rect.size
        # alien_width = alien.rect.width              # get the alien's width and store it to the variable 'alien_width'
        available_space_x = self.settings.screen_width - (2 * alien_width)  # calculate the required space...
        number_aliens_x = available_space_x // (2 * alien_width)               # and the number of possible aliens in that space

        # determine the number of alien rows that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create the first full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):            # for however many aliens we can have (calc'ed above)
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):            
        """ create an alien and place it in the row """
        alien = Alien(self)                         # create an alien and....
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number      # determine where it goes on the x axis
        alien.rect.x = alien.x                      # assign that value to the alien image
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)                  # then add each alien to the group of aliens
        # make an alien
        # alien = Alien(self)     # create an instance of alien from the class
        # self.aliens.add(alien)   # add it to the list of aliens

    def _check_fleet_edges(self):
        """ respond when aliens reach the edge of screen """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ drop the entire fleet and change direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """ updates images on the screen, and flips to a new screen """
        self.screen.fill(self.settings.bg_colour)        # with settings imported from Settings class
        self.ship.blitme()          # draw the ship on the screen, on top of the background
        for bullet in self.bullets.sprites():       # returns a list of all the bullets...
            bullet.draw_bullet()                    # call 'draw bullet' in bullet.py
        self.aliens.draw(self.screen)       # 'draw' draws each element in the position defined by its rect attribute

        # draw the score information
        self.sb.show_score()

        # draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    
if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()


