import pygame.font      # allows us to render text to the screen

class Button:

    def __init__(self, ai_game, msg):
        """ initialise button attributes """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_colour = (237, 133, 64)
        self.text_colour = (247, 241, 238)
        self.font = pygame.font.SysFont(None, 48)       # font and size

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ turn the message into a rendered image and center the text on the button """
        self.msg_image = self.font.render(msg, True, self.text_colour, 
                            self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ draw a blank button, then the message """
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)