from turtle import *
from ball import Ball

# Set up the screen
window = Screen()
window.bgcolor("white")

# Create three turtle objects with different colors
ball1 = Ball("yellow")
ball2 = Ball("purple")
ball3 = Ball("pink")

# Set the number of animation iterations
x = 36

# Draw and rotate the shapes
while x > 0:

    ball2.draw_circle()
    ball2.turn_left()

    ball3.draw_square()
    ball3.turn_left()

    x -= 1

# Keep the window open until clicked
window.exitonclick()