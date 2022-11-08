from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 260)
        self.write(f"{self.player_1_score} : {self.player_2_score}", align=ALIGNMENT, font=FONT)

    def update(self, x_cor):
        self.clear()
        if x_cor > 0:
            self.player_1_score += 1
        else:
            self.player_2_score += 1
        self.write(f"{self.player_1_score} : {self.player_2_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
