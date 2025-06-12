import turtle

if turtle.ycor() < 0:
 turtle.goto(0, 0)

if turtle.xcor() > 100 and turtle.xcor() < 200:
    turtle.goto(300, 0)
turtle.done()  # Finish the turtle graphics