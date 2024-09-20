from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.timmy = []
        self.create_snake()
        self.head =self.timmy[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_timmy(position)


    def add_timmy(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.timmy.append(tim)

    def extend(self):
        #add new length to snake
        self.add_timmy(self.timmy[-1].position())


    def move(self):
        for seg_num in range(len(self.timmy) -1, 0, -1):
            new_x = self.timmy[seg_num - 1].xcor()
            new_y = self.timmy[seg_num - 1].ycor()
            self.timmy[seg_num].goto(new_x, new_y)
        self.timmy[0].forward(MOVE_DISTANCE)

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



