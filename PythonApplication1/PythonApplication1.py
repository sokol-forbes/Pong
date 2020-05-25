import turtle

window = turtle.Screen()
window.title("Ping-pong")
window.setup(width=1.0,height=1.0) #весь экран
window.bgcolor("black")

border = turtle.Turtle()
border.speed(50)
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

#border.goto(0,-300)

window.mainloop()