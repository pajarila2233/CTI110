import turtle

# Create turtle object
t = turtle.Turtle()
t.shape('turtle')

# Set pen color and size
t.pencolor("purple")
t.pensize(3)

# Draw first initial "A"
t.left(75)
t.forward(100)
t.right(150)
t.forward(100)
t.penup()
t.right(180)
t.forward(50)
t.left(75)
t.pendown()
t.forward(25)

# Move turtle to draw second initial "P"
t.penup()
t.goto(100, 0)
t.pendown()

# Draw second initial "P"
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Exit window when clicked
turtle.exitonclick()
