from turtle import Turtle

FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.level}", FONT)
        self.goto(-250, 250)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(-200, 0)
        self.write(f"GAME OVER: {self.level}", font=FONT)
