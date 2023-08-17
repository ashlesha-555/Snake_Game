from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.segments.append(square)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)