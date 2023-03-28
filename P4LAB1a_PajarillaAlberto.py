import turtle

# Create turtle object
t = turtle.Turtle()
t.shape('turtle')
t.pensize(2)
t.pencolor('green')

# Draw square
count = 0
while count < 4:
    t.forward(100)
    t.right(90)
    count += 1

# Move turtle to draw triangle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw triangle
count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

# Exit window when clicked
turtle.exitonclick()
