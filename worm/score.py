from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.teleport(0, 360)
        self.hideturtle()
        self.score_value = 0
        self.high_score_value = 0
        self.get_high_score_value()
        self.update_score()
        self.create_divider() # Prevents the worm from being overlayed agaist the score
        
    def create_divider(self):
        # Top
        divider = Turtle(visible=False)
        divider.color('white')
        divider.hideturtle()
        divider.teleport(-1000, 350)
        divider.goto(1000, 350)   
        # Right
        divider2 = Turtle(visible=False)
        divider2.color('white')
        divider2.hideturtle()
        divider2.teleport(410, -1000)
        divider2.goto(410, 1000) 
        # Left
        divider3 = Turtle(visible=False)
        divider3.color('white')
        divider3.hideturtle()
        divider3.teleport(-410, -1000)
        divider3.goto(-410, 1000) 
        
    def update_score(self):
        self.clear()
        self.write(
            arg=f'Score: {self.score_value} High Score: {self.high_score_value}',
            align='center',
            font=('Monospace', 18, 'bold')
        )
        
    def increase_score(self, value=1):
        self.score_value += value
        self.update_score()
        
    def get_high_score_value(self):
        with open('worm/highscore.txt', 'r') as file:
            self.high_score_value = int(file.read())
        
    def reset_score(self):
        if self.score_value > self.high_score_value:
            high_score_value = self.score_value
            with open('worm/highscore.txt', 'w') as file:
                file.write(f'{high_score_value}')
            
        self.score_value = 0
        self.get_high_score_value()
        self.update_score()