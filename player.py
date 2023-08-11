from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.starting_position()
        self.setheading(90)
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def starting_position(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finih_line(self):
        if self.ycor()>280:
            return True
        else:
            False
        
