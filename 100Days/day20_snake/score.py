from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ("Arial", 28, "bold")


class Score(Turtle):
    """Generates & updates the game score."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 295)
        self.update_scoreboard()


    def update_scoreboard(self):
        """Updates the scoreboard every time the score changes."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        """Increase the score once food is eaten"""
        self.score += 10
        self.clear()
        self.update_scoreboard()
