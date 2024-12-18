import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

#########################################################
# Move a turtle
pen.penup()
pen.goto(-400,0)
pen.pendown()

# Draw a square 1
for i in range(4):
    pen.forward(50)
    pen.right(90)

# Move a turtle
pen.penup()
pen.goto(-300,0)
pen.pendown()

# Draw a square 2
for i in range(4):
    pen.forward(50)
    pen.right(90)
###############################################################

# Move a turtle
pen.penup()
pen.goto(-200,0)
pen.pendown()

# Draw a triangle 1
for i in range(3):
    pen.forward(50)
    pen.right(120)

# Move a turtle
pen.penup()
pen.goto(-100,0)
pen.pendown()

# Draw a triangle 2
for i in range(3):
    pen.forward(50)
    pen.right(120)

###############################################################

# Move a turtle
pen.penup()
pen.goto(0,0)
pen.pendown()

# Draw a rectangle 1
for i in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
###############################################################

# Move a turtle
pen.penup()
pen.goto(200,0)
pen.pendown()

# Draw a rectangle 2
for i in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)

###############################################################

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()