import turtle

screen = turtle.Screen()  # Get the screen object

if screen.bgcolor() == 'white':
    screen.bgcolor('red')  # Change the background color to red if it's white


if turtle.pensize() < 5:
    turtle.pensize(5)  # Set the pen size to 5 if it's less than 5

turtle.hideturtle()  # Hide the turtle cursor for a cleaner look
turtle.color('deeppink', 'pink')  # Set outline and fill color
turtle.up()
turtle.goto(0, -100)  # Center the heart vertically
turtle.down()
turtle.begin_fill()
turtle.left(140)
turtle.forward(180)

for _ in range(200):
    turtle.right(1)
    turtle.forward(2)
turtle.left(120)

for _ in range(200):
    turtle.right(1)
    turtle.forward(2)
    
turtle.forward(180)
turtle.end_fill()

turtle.done()  # Finish the turtle graphics