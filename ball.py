from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()



    def move_ball(self):
        self.goto(x=int(self.xcor() + self.x_move), y=int(self.ycor() + self.y_move))


    def bounce(self):
        self.y_move *= -1

    def pedal_bounce(self):
        self.x_move *= -1