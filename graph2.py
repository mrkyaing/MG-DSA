import turtle

turtle.setheading(128)  # Set the turtle's heading to 128 degrees
if turtle.heading()>90 and turtle.heading()<270:
    turtle.setheading(180)
turtle.done   # Set the turtle's heading to 90 degrees if it's between 90 and 270 degrees