from turtle import Turtle


FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    """Generates & updates the game score."""
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_score()


    def update_score(self):
        """Increase the score once food is eaten"""
        self.clear()
        self.level += 1
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        """Displays "GAME OVER"and the score."""
        self.goto(0,0)
        self.write(f"GAME OVER\nScore: {(self.level) - 1}", align="center", font=FONT)        