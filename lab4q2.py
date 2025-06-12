import turtle

# Set up the turtle
t = turtle.Turtle()
side = 1
f=100
# Draw the first side
if side == 1:
    t.forward(f)
    t.left(120)
    side = 2

# Draw the second side
if side == 2:
    t.forward(f)
    t.left(120)
    side = 3

# Draw the third side
if side == 3:
    t.forward(f)
    t.left(120)
    side = 4

# Keep the window open until closed by the user
turtle.done()
