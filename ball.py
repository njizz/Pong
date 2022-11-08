from turtle import Turtle
INITIAL_RATE = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fast")
        self.x_rate = INITIAL_RATE
        self.y_rate = INITIAL_RATE

    def move(self):
        new_x = self.xcor() + self.x_rate
        new_y = self.ycor() + self.y_rate
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_rate *= -1

    def bounce_x(self, increase):
        self.x_rate *= -1
        if increase:
            self.y_rate *= 1.2
            self.x_rate *= 1.2

    def reset(self):
        self.goto(0, 0)
        self.bounce_x(False)
        self.x_rate = INITIAL_RATE
        self.y_rate = INITIAL_RATE


