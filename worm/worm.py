from turtle import Turtle


class Worm:
    INITIAL_COORDINATES = [(0,0), (-20,0), (-40,0)]
    MOVE_DISTANCE = 20
    def __init__(self):
        self.worm_segments = []
        self.create_worm()
        
    def _add(self, x, y):
        worm = Turtle('square')
        worm.color('lime')
        worm.penup()
        worm.goto(x, y)
        self.worm_segments.append(worm)
        
    def create_worm(self):
        for coor in self.INITIAL_COORDINATES:
            self._add(coor[0], coor[1])
            
    def move(self):
        for i in range(len(self.worm_segments)-1, 0, -1):
            x = self.worm_segments[i-1].xcor()
            y = self.worm_segments[i-1].ycor()
            self.worm_segments[i].goto(x, y)
        self.worm_segments[0].forward(self.MOVE_DISTANCE)
        self.return_to_screen()
        
    def return_to_screen(self):
        x = self.worm_segments[0].xcor()
        y = self.worm_segments[0].ycor()
        if self.worm_segments[0].xcor() > 400:
            self.worm_segments[0].goto(-350, y)
        if self.worm_segments[0].ycor() > 400:
            self.worm_segments[0].goto(x, -350)
        if self.worm_segments[0].xcor() < -400:
            self.worm_segments[0].goto(350, y)
        if self.worm_segments[0].ycor() < -400:
            self.worm_segments[0].goto(x, 350)
            
    def turn_up(self):
        if self.worm_segments[0].heading() != 270.0:
            self.worm_segments[0].setheading(90)
            
    def turn_down(self):
        if self.worm_segments[0].heading() != 90.0:
            self.worm_segments[0].setheading(270)
            
    def turn_left(self):
        if self.worm_segments[0].heading() != 0.0:
            self.worm_segments[0].setheading(180)
            
    def turn_right(self):
        if self.worm_segments[0].heading() != 180.0:
            self.worm_segments[0].setheading(0)