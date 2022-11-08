from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('P O N G')
screen.tracer(0)

player_1 = Paddle('player_1')
player_2 = Paddle('player_2')
ball = Ball()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkeypress(player_1.move_up, "w")
screen.onkeypress(player_1.move_down, "s")
screen.onkeypress(player_2.move_up, "Up")
screen.onkeypress(player_2.move_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # detect collision with wall
    if abs(ball.ycor()) >= 290:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(player_1) < 50 or ball.distance(player_2) < 50) and abs(ball.xcor()) > 330:
        ball.bounce_x(True)

    # detect ball going out of bounds
    if abs(ball.xcor()) >= 400:
        scoreboard.update(ball.xcor())
        ball.reset()
        screen.onkey(ball.move, "space")


scoreboard.game_over()







screen.exitonclick()