from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    """Generates & updates the game score."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("100Days\day24_snakeupdated/data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        """Updates the scoreboard every time the score changes."""
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        """Updates the high score"""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("100Days\day24_snakeupdated/data.txt", mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard


    def update_score(self):
        """Increase the score once food is eaten"""
        self.score += 10
        self.update_scoreboard()
