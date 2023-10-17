from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.penup()
        self.refresh()

    def refresh(self):
        pos_x = randint(-280, 280)
        pos_y = randint(-280, 270)
        self.goto(pos_x, pos_y)