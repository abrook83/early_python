from turtle import Turtle
L_ALIGNMENT = (-330, 270)
R_ALIGNMENT = (330, 270)
C_ALIGNMENT = "Center"
FONT = ("Arial", 28, "bold")


class Scores(Turtle):
    """Generates & updates the game score."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_player_score = 0
        self.r_player_score = 0
        self.update_score()


    def update_score(self):
        """Increase the score once food is eaten"""
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_player_score, align="center", font=FONT)
        self.goto(100, 240)
        self.write(self.r_player_score, align="center", font=FONT)


    def update_l_score(self):
        """Updates the left player's scoreboard every time the score changes."""
        self.l_player_score += 1
        self.update_score()

    
    def update_r_score(self):
        """Updates the right player's scoreboard every time the score changes."""
        self.r_player_score += 1  
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=C_ALIGNMENT, font=FONT)



