from turtle import Turtle
PLAYER_1_START_POSITION = (-350, 0)
PLAYER_2_START_POSITION = (350, 0)
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.player = player
        if self.player == 'player_1':
            self.goto(PLAYER_1_START_POSITION)
        elif self.player == 'player_2':
            self.goto(PLAYER_2_START_POSITION)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)
