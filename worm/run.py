from worm import Worm
from turtle import Screen
from time import sleep


worm = Worm()
screen = Screen()
screen.screensize(canvheight=400, canvwidth=400, bg='black')
screen.tracer(0)
screen.listen()
screen.onkey(worm.turn_up, 'Up')
screen.onkey(worm.turn_down, 'Down')
screen.onkey(worm.turn_left, 'Left')
screen.onkey(worm.turn_right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)
    worm.move()


screen.exitonclick()