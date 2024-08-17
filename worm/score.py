from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.teleport(0, 360)
        self.hideturtle()
        self.score_value = 0
        self.write(
            arg=f'Score: {self.score_value}',
            align='center',
            font=('Monospace', 20, 'normal')
        )
        self.create_divider() # Prevents the worm from being overlayed agaist the score
        
    def create_divider(self):
        divider = Turtle(visible=False)
        divider.color('white')
        divider.hideturtle()
        divider.teleport(-1000, 350)
        divider.goto(1000, 350)
        
    def increase_score(self, value=1):
        self.score_value += value
        self.clear()
        self.write(
            arg=f'Score: {self.score_value}',
            align='center',
            font=('Monospace', 20, 'normal')
        )