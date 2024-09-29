import turtle
class Xiao:
    def __init__(self):
        self.segment = []
        self.section = 3
        self.create_snake()
        self.GOUP = False
        self.TURNLEFT = False
        self.TURNRIGHT = False
        self.GODOWN = False
    def activate_down(self):
        self.GODOWN = True

    def activate_right(self):
        self.TURNRIGHT = True

    def activate_left(self):
        self.TURNLEFT = True

    def activate_up(self):
        self.GOUP = True
    def create_snake(self):
        self.position_origin = 20
        for number_snake in range(self.section):
            snake = turtle.Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.setposition(self.position_origin - 20, 0)
            self.position_origin -= 20
            self.segment.append(snake)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)
        for a in range(len(self.segment)):
            if self.GOUP and self.segment[0].heading() != 90 and self.segment[0].heading() != 270 and a == 0:
                self.segment[0].setheading(90)
            elif self.TURNLEFT and self.segment[0].heading() != 180 and self.segment[0].heading() != 0 and a == 0:
                self.segment[0].setheading(180)
            elif self.TURNRIGHT and self.segment[0].heading() != 0 and self.segment[0].heading() != 180 and a == 0:
                self.segment[0].setheading(0)
            elif self.GODOWN and self.segment[0].heading() != 270 and self.segment[0].heading() != 90 and a == 0:
                self.segment[0].setheading(-90)
    def fatter(self):
        if self.segment[len(self.segment) - 1].heading() == 0:
            snake = turtle.Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.setposition(self.segment[len(self.segment) - 1].xcor() - 20, self.segment[len(self.segment) - 1].ycor())
            self.segment.append(snake)
        elif self.segment[len(self.segment) - 1].heading() == 90:
            snake = turtle.Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.setposition(self.segment[len(self.segment) - 1].xcor() , self.segment[len(self.segment) - 1].ycor() - 20)
            self.segment.append(snake)
        elif self.segment[len(self.segment) - 1].heading() == 180:
            snake = turtle.Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.setposition(self.segment[len(self.segment) - 1].xcor() + 20, self.segment[len(self.segment) - 1].ycor())
            self.segment.append(snake)
        elif self.segment[len(self.segment) - 1].heading() == 270:
            snake = turtle.Turtle()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.setposition(self.segment[len(self.segment) - 1].xcor() , self.segment[len(self.segment) - 1].ycor() + 20)
            self.segment.append(snake)
    def reset(self):
        for i in self.segment:
            i.hideturtle()
        self.segment.clear()
        self.create_snake()