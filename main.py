from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
import time
from score import Scoreboard
window=Screen()
window.setup(width=800,height=600)
window.bgcolor("black")
window.tracer(0)
r_pdl=Paddle((350,0))
l_pdl=Paddle((-350,0))
ball=Ball()
score=Scoreboard()
window.listen()
window.onkey(r_pdl.move_up,"Up")
window.onkey(r_pdl.move_down,"Down")
window.onkey(l_pdl.move_up,"s")
window.onkey(l_pdl.move_down,"w")
GAME_ON=True
DEFAULT_SPEED=0.1
while GAME_ON:
    window.update()
    time.sleep(DEFAULT_SPEED)
      # تحريك الكرة
    ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
    # ادا اصطدمت الكرة في الجدران من جهة الاعلى او الاسفل
    if ball.ycor()>= 280 or ball.ycor() <= -280:
        ball.y_move*=-1
    # ادا صدمت الكرة في احد المضارب
    if (ball.xcor() >= 330 and ball.distance(r_pdl) <= 50 )or (ball.xcor() <= -330 and ball.distance(l_pdl)<= 50):
        ball.x_move*=-1
        DEFAULT_SPEED*=0.9
    # ادا خرجت الكرة من جهة اليمين
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.x_move*=-1
        score.l_point()
        DEFAULT_SPEED=0.1
    # ادا خرجت الكرة من جهة اليسار
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_move*=-1
        score.r_point()
        DEFAULT_SPEED=0.1


window.exitonclick()
