from turtle import Screen
from paddle import Padel
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

XCOR1 = int(screen.window_width() / 2 - 50)
XCOR2 = -int(screen.window_width() / 2 - 50)
TOP = int(screen.window_height() / 2 - 20)
BOTTOM = -int(screen.window_height() / 2)
SPEED = 0.05

print(XCOR1, XCOR2)
padel1 = Padel(XCOR1, 0)
padel2 = Padel(XCOR2, 0)


#time.sleep(0.05)

screen.listen()
screen.onkey(padel1.up, "Up")
screen.onkey(padel1.down,  "Down")
screen.onkey(padel2.up, "w")
screen.onkey(padel2.down,  "s")

ball = Ball()
score = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED)
    ball.move_ball()

    if ball.ycor() > TOP or ball.ycor() < BOTTOM:
        ball.bounce()

    if ball.distance(padel1) < 50 and ball.xcor() > 320:
        ball.pedal_bounce()
        if SPEED > 0.021:
            SPEED -= 0.005
            print(SPEED)

    if ball.distance(padel2) < 50 and ball.xcor() < -320:
        ball.pedal_bounce()
        if SPEED > 0.021:
            SPEED -= 0.005
            print(SPEED)

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.x_move *= -1
        score.lscore +=1
        score.clear()
        score.score_update()
        SPEED = 0.05

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.x_move *= -1
        score.rscore += 1
        score.clear()
        score.score_update()
        SPEED = 0.05


screen.exitonclick()