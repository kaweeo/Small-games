from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        #            self.setpos(x=X, y=0)
        #            self.onkey(fun, key=)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
