class Settings:
    """ A class to store all the game's settings """

    def __init__(self):
        """ initialise the game's static settings """
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 95, 135)     

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15        
        self.bullet_colour = (255,183,75)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien points icreases
        self.score_scale = 1.5
        
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """ initialise settings the change as game progresses """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """ increase speed settings & point values """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
         