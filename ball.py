from turtle import *

# Create a Ball class using Turtle
class Ball(Turtle):

    # Initialize the turtle
    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.pensize(2)
        self.speed(0)

    # Move the turtle diagonally
    def move(self):
        x = self.xcor() + 50
        y = self.ycor() + 50
        self.goto(x, y)

    # Draw a circle
    def draw_circle(self):
        self.circle(75)

    # Draw a square
    def draw_square(self):
        for i in range(4):
            self.forward(160)
            self.left(90)

    # Rotate the turtle to the left
    def turn_left(self):
        self.left(10)