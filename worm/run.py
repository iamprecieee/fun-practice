from worm import Worm
from food import Food
from score import Score
from turtle import Screen
from time import sleep
from datetime import datetime

worm = Worm()
screen = Screen()
screen.screensize(canvheight=400, canvwidth=400, bg='black')
screen.tracer(0)
screen.listen()
screen.onkey(worm.turn_up, 'Up')
screen.onkey(worm.turn_down, 'Down')
screen.onkey(worm.turn_left, 'Left')
screen.onkey(worm.turn_right, 'Right')

score = Score()
food = Food()
mega_food_count = 0
is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.05)
    worm.move()
    
    if len(food.current_time) != 0 and datetime.now() > food.current_time[0]:
        food.revert_mega_food()
    
    if worm.worm_segments[0].distance(food) < 20:
        if food.color() == ('red', 'red'):
            score.increase_score(value=5)
            food.revert_mega_food()
            food.feed_count = 0
            worm.increase_length(5)
        else:
            score.increase_score()
            food.feed_count += 1
            food.pause_mega = False
            worm.increase_length()
            
        food.change_position()
        
    if all([food.feed_count != 0, food.feed_count % 2 == 0, not food.pause_mega]):
        food.create_mega_food()
        
    for segment in worm.worm_segments[1:]:
        if worm.worm_segments[0].distance(segment) < 10:
            score.reset_score()
    

screen.exitonclick()
