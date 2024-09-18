from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake():
    def __init__(self) -> None: 
        self.tail = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.new_tail(position)

    def snake_reset(self):
        for each in self.tail:
            each.goto(1000,1000)
        self.tail.clear()
        self.create_snake()


    def new_tail(self,position):
        new_piece = Turtle("square")
        new_piece.penup()
        new_piece.color("white")
        new_piece.goto(position)
        self.tail.append(new_piece)

    def extends(self):
        self.new_tail(self.tail[-1].position())

    def move(self):
        for tail_num in range(len(self.tail) - 1, 0, -1):
            new_x = self.tail[tail_num - 1].xcor()
            new_y = self.tail[tail_num - 1].ycor()
            self.tail[tail_num].goto(new_x, new_y)
        
        self.tail[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.tail[0].heading() != DOWN:
            self.tail[0].setheading(UP)
    
    def left(self):
        if self.tail[0].heading() != RIGHT:
            self.tail[0].setheading(LEFT)
    
    def right(self):
        if self.tail[0].heading() != LEFT:
            self.tail[0].setheading(RIGHT)

    def down(self):
        if self.tail[0].heading() != UP:
            self.tail[0].setheading(DOWN)