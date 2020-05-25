import turtle
from random import choice, randint


window = turtle.Screen()
window.title("Ping-pong")
window.setup(width=1.0,height=1.0) #весь экран
window.bgcolor("black")

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


def move_up_left():
    y = rocket_left.ycor() + 10
    if y > 250:
        y = 250 
    rocket_left.sety(y )

def move_down_left():

    y = rocket_left.ycor() - 10
    if y < -250:
        y = -250
    rocket_left.sety(y)


rocket_right = turtle.Turtle()
rocket_right.color("sky blue")
rocket_right.shape("square")
rocket_right.shapesize(stretch_len=1,stretch_wid=5)
rocket_right.penup()
rocket_right.goto(450,0)

def move_up_right():
    y = rocket_right.ycor() + 10
    if y > 250:
        y = 250 
    rocket_right.sety(y)

def move_down_right():

    y = rocket_right.ycor() - 10
    if y < -250:
        y = -250
    rocket_right.sety(y)

ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.shapesize(stretch_wid = 2, stretch_len = 2)
ball.color("deeppink")
ball.dx = 3
ball.dy = 3
ball.penup()


window.listen()
window.onkeypress(move_up_left,"w")
window.onkeypress(move_down_left,"s")

window.onkeypress(move_up_right,"j")
window.onkeypress(move_down_right,"n")


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 280 :
        ball.dy = - ball.dy
    if ball.ycor() <= -280 :
        ball.dy = - ball.dy
    if ball.xcor() >= 480 :
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2,2,3,4])
        ball.dy = choice([-4,-3,-2,2,3,4])
    if ball.xcor() <= -480 :
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4,-3,-2,2,3,4])
        ball.dy = choice([-4,-3,-2,2,3,4])

#border.goto(0,-300)

window.mainloop()