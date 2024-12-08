
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=750)
screen.title("Ping Pong")
screen.tracer(0)

ball = Ball()
l_paddle = Paddle(-350)
r_paddle = Paddle(350)
score = ScoreBoard()

screen.listen()

screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.recoil()

    if ball.xcor() > 360 and ball.distance(r_paddle) > 50:
        score.l_point()
        time.sleep(1.5)
        ball.reset()
        ball.recoil()

    elif ball.distance(l_paddle) > 50 and ball.xcor() < -360:
        score.r_point()
        time.sleep(1.5)
        ball.reset()
        ball.recoil()
        
    if score.game_over():
        game_on = False

screen.exitonclick()
