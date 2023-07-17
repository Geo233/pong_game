from turtle import Turtle, Screen

class Padel(Turtle):

    def __init__(self, x, y):
         super().__init__()
         self.screen = Screen()
         self.p1 = self.create_padel(x, y)


    def create_padel(self, x, y):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len = 1, stretch_wid= 5)
        self.goto(x, y)
        return self



    def up(self):
        #self.p1.setheading(90)
        self.p1.goto(x=self.p1.xcor(), y=int(self.p1.ycor() + 30))

    def down(self):
       #self.p1.setheading(270)
        self.p1.goto(x = self.p1.xcor(), y = int(self.p1.ycor() - 30))