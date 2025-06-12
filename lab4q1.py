import turtle

screen_length = 50

def draw_square(length):
    sides_drawn = 0
    if sides_drawn == 0:
        turtle.forward(length)
        turtle.right(90)
        sides_drawn += 1
    if sides_drawn == 1:
        turtle.forward(length)
        turtle.right(90)
        sides_drawn += 1
    if sides_drawn == 2:
        turtle.forward(length)
        turtle.right(90)
        sides_drawn += 1
    if sides_drawn == 3:
        turtle.forward(length)
        turtle.right(90)
        sides_drawn += 1

if turtle.pensize() < 5:
    turtle.pensize(5)  # Set the pen size to 5 if it's less than 5
    turtle.color('black')
if turtle.bgcolor() == 'white':
    turtle.bgcolor('red')  # Change the background color to red if it's white
    
draw_square(screen_length)
turtle.hideturtle()  # Hide the turtle cursor for a cleaner look
turtle.done()  # Finish the turtle graphics

