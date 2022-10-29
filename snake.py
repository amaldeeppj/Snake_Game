from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.shapesize(stretch_wid=1, stretch_len=1.5)
        new_segment.penup()
        new_segment.color("black", "firebrick")
        new_segment.pen(outline=10)
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            new_heading = self.segments[segment - 1].heading()
            self.segments[segment].goto(x=new_x, y=new_y)
            self.segments[segment].setheading(new_heading)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_reset(self):
        for segment in self.segments:
            segment.goto(2000, 2000)
            segment.clear()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]





