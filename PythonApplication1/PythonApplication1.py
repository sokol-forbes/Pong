import turtle
from random import choice, randint


window = turtle.Screen()
window.title("Ping-pong")
window.setup(width=1.0,height=1.0) #весь экран
window.bgcolor("black")
window.tracer(2)

border = turtle.Turtle()   #начальная отрисовка поля
border.speed(0)
border.color("yellow")
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0,300)      #отрисовка сетки
border.color("red")
border.setheading(270)
for i in range(25):
    if i%2==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

border.hideturtle()


rocket_left = turtle.Turtle()          #отрисовка левой ракетки
rocket_left.color("blue")
rocket_left.shape("square")
rocket_left.shapesize(stretch_len=1,stretch_wid=5)
rocket_left.penup()
rocket_left.goto(-450,0)


def move_up_left():                         #перемещение вверх левой ракетки
    y = rocket_left.ycor() + 10
    if y > 250:
        y = 250 
    rocket_left.sety(y )

def move_down_left():                       #перемещение вниз левой ракетки

    y = rocket_left.ycor() - 10
    if y < -250:
        y = -250
    rocket_left.sety(y)


rocket_right = turtle.Turtle()               #отрисовка правой ракетки
rocket_right.color("sky blue")
rocket_right.shape("square")
rocket_right.shapesize(stretch_len=1,stretch_wid=5)
rocket_right.penup()
rocket_right.goto(450,0)

FONT = ("Arial",44)
score_left = 0
s1 = turtle.Turtle(visible=False)
s1.color("dark green")
s1.penup()
s1.setposition(200,300)
s1.write(score_left,font = FONT)
score_right = 0
s2 = turtle.Turtle(visible=False)
s2.color("dark green")
s2.penup()
s2.setposition(-200,300)
s2.write(score_left,font = FONT)


def move_up_right():                        #перемещение вверх правой ракетки
    y = rocket_right.ycor() + 10
    if y > 250:
        y = 250 
    rocket_right.sety(y)

def move_down_right():                      #перемещение вниз правой ракетки

    y = rocket_right.ycor() - 10
    if y < -250:
        y = -250
    rocket_right.sety(y)

ball = turtle.Turtle()                      #отрисовка шарика
ball.shape("circle")
ball.speed(0)
ball_size = 10
ball.shapesize(stretch_wid = (ball_size/10), stretch_len = (ball_size/10))
ball.color("deeppink")
ball.dx = 2
ball.dy = 2
ball.penup()


window.listen()                                     #вызов функций перемещения ракеток
window.onkeypress(move_up_left,"w")
window.onkeypress(move_up_left,"W")
window.onkeypress(move_down_left,"s")
window.onkeypress(move_down_left,"S")
window.onkeypress(move_up_right,"Up")
window.onkeypress(move_down_right,"Down")


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)                #движение шарика
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >=  300 - ball_size :
        ball.dy = - ball.dy
    if ball.ycor() <= -300 + ball_size:
        ball.dy = - ball.dy
    if ball.xcor() >= (500 - ball_size) :
        score_right +=1
        s2.clear()
        s2.write(score_right,font = FONT)
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-3,-2,-1,1,2,3])
        ball.dy = choice([-3,-2,-1,1,2,3])
    if ball.xcor() <= -500 + ball_size :
        score_left +=1
        s1.clear()
        s1.write(score_left,font = FONT)
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-3,-2,-1,1,2,3])
        ball.dy = choice([-3,-2,-1,1,2,3])
    
    if ball.ycor() >= rocket_right.ycor()-50 and ball.ycor() <= rocket_right.ycor()+50 \
            and ball.xcor() <= rocket_right.xcor()+5 and ball.xcor() >= rocket_right.xcor()-5:
            ball.dx = - ball.dx
    if ball.ycor() >= rocket_left.ycor()-50 and ball.ycor() <= rocket_left.ycor()+50 \
            and ball.xcor() <= rocket_left.xcor()+5 and ball.xcor() >= rocket_left.xcor()-5:
            ball.dx = - ball.dx

#border.goto(0,-300)

window.mainloop()