###
# Draw a square
#
def draw_square(length):
    import turtle

    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = (length)

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

# Draw a triangle
#
def draw_triangle(length):
    import turtle

    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = (length)

    # Draw a triangle
    for i in range(3):
        pen.forward(side_length)
        pen.right(120)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

# Draw a rectangle
#
def draw_rectangle(lenght_a, lenght_b):
    import turtle

    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Draw a rectangle
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)


    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()