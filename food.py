from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.shape("circle")
        self.refresh()
    def refresh(self):
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-280, 270)
        self.teleport(x_coordinate, y_coordinate)