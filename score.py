from turtle import Turtle


ALIGN = "center"
FONT = ("courier", 30, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.high_score = self.check_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score_board()

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()
        self.score = 0
        self.score_board()
        
    def check_score(self):
        with open("data.txt") as data_score:
            contents = int(data_score.read())
            return contents
    
    def new_high_score(self):
        with open("data.txt", mode='w') as write_score:
            contents = str(self.score)
            write_score.write(contents)

        
    def score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("You Lose.", align=ALIGN, font=FONT)

    def add(self):
        self.score += 1
        self.score_board()

    def score_reset(self):
        self.update_score()

     

        
