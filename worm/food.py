from turtle import Turtle
from random import randint
# from time import sleep, time
from datetime import datetime, timedelta


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.teleport(randint(-300, 300), randint(-300, 300))
        self.feed_count = 0 # Controls the score interval for mega food creation
        self.current_time = [] # Sets the duration for mega food state
        self.pause_mega = False # Prevents looped creation of mega food
        
    def change_position(self):
        self.teleport(randint(-300, 300), randint(-300, 300))
    
    def create_mega_food(self):
        '''
        Creates a time-limited mega food.
        '''
        self.color('red')
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        if len(self.current_time) == 0:
            self.current_time.append(datetime.now() + timedelta(seconds=5))
        self.pause_mega = True
        
    def revert_mega_food(self):
        '''
        Returns mega food to its original state.
        '''
        self.color('yellow')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.current_time.clear()