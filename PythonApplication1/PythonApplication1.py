import turtle

window = turtle.Screen()
window.title("Ping-pong")
window.setup(width=1.0,height=1.0) #весь экран
window.bgcolor("black")

border = turtle.Turtle()
border.speed(0)
border.color("yellow")
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0,300)
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


rocket_a = turtle.Turtle()
rocket_a.color("blue")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1,stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450,0)


def move_up_left():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250 
    rocket_a.sety(y )

def move_down_left():

    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


rocket_b = turtle.Turtle()
rocket_b.color("blue")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1,stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450,0)

def move_up_right():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250 
    rocket_b.sety(y)

def move_down_right():

    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)





window.listen()
window.onkeypress(move_up_left,"w")
window.onkeypress(move_down_left,"s")

window.onkeypress(move_up_right,"j")
window.onkeypress(move_down_right,"n")





#border.goto(0,-300)

window.mainloop()