import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(x, y)
