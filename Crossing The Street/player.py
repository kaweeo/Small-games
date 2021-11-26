from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.lt(90)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y=new_y)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False