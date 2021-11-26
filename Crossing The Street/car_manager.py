from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
STAMP_SIZE = 20
random_color = COLORS[random.randint(0, 5)]

#print(random_position)

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-280, 280)
            new_car.goto(280, random_y)
            new_car.shapesize(20 / STAMP_SIZE, 40 / STAMP_SIZE)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def incr_speed(self):
        self.car_speed += MOVE_INCREMENT