import turtle
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.highscore = 0
        self.teleport(-280, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.point}, highest score: {self.highscore}", False, "left", ("Arial", 16, "normal"))
    def high_score(self):
        if self.point > int(self.highscore):
            with open("score.txt", mode = "w") as file:
                file.write(str(self.point))
            with open("score.txt", mode = "r") as file:
                self.highscore = file.read()
        self.point = 0
    def after_reset(self):
        self.clear()
        self.write(f"Score: {self.point}, highest score: {self.highscore}", False, "left", ("Arial", 16, "normal"))
    def increase(self):
        self.point += 1
        self.clear()
        self.write(f"Score: {self.point}, highest score: {self.highscore}", False, "left", ("Arial", 16, "normal"))