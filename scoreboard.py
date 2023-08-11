from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level =1 
        self.goto(-200,250)
        self.current_level()
        
    
    def current_level(self):
        self.write(f' Level: {self.level}',align='center',font=FONT)
    
    def next_level(self):
        self.clear()
        self.level +=1
        self.current_level()
    
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write('Game Over',align='center',font=FONT)




