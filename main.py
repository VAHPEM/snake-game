import turtle
import time
import snake
import food
import scoreboard
xiao = snake.Xiao()
performance = turtle.Screen()
performance.setup(width=600, height=600)
performance.bgcolor("black")
performance.tracer(0)
performance.title("Snake Game")
performance.listen()
performance.onkey(key="s", fun=xiao.activate_down)
performance.onkey(key="w", fun=xiao.activate_up)
performance.onkey(key="a", fun=xiao.activate_left)
performance.onkey(key="d", fun=xiao.activate_right)
game_is_on = True
growth = food.Food()
score = scoreboard.Score()
while game_is_on == True:
    xiao.GOUP = False
    xiao.TURNLEFT = False
    xiao.TURNRIGHT = False
    xiao.GODOWN = False
    performance.update()
    time.sleep(0.1)
    xiao.move()
    if xiao.segment[0].distance(growth) <= 15:
        growth.refresh()
        xiao.fatter()
        score.increase()
    if xiao.segment[0].xcor() >= 300 or xiao.segment[0].xcor() <= -300 or xiao.segment[0].ycor() >= 300 or xiao.segment[0].ycor() <= -300:
        score.high_score()
        score.after_reset()
        xiao.reset()
    for c in xiao.segment[2: len(xiao.segment)]:
        if xiao.segment[0].distance(c) <= 10:
            score.high_score()
            score.after_reset()
            xiao.reset()
performance.exitonclick()