from turtle import Turtle, Screen
from paddle_player import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("P-O-N-G")
screen.tracer(0)


p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1.move_up, "Up")
screen.onkey(p1.move_down, "Down")
screen.onkey(p2.move_up, "w")
screen.onkey(p2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()
    #Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detech of the bounds
    if ball.xcor() > 400:
        ball.reset_position()
        ball.x_step = -10
        ball.y_step = -10
        scoreboard.l_point()

    elif ball.xcor() < -400:
        ball.reset_position()
        ball.x_step = 10
        ball.y_step = 10
        scoreboard.r_point()

screen.exitonclick()