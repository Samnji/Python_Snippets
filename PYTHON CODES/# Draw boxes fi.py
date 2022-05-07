# Draw boxes filled with different colors

import turtle

turtle.color("black", "red")
turtle.begin_fill()

for i in range(4):
	turtle.forward(70)
	turtle.delay(10)
	turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()

for i in range(4):
	turtle.forward(70)
	turtle.delay(10)
	turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()

for i in range(4):
	turtle.forward(70)
	turtle.delay(10)
	turtle.right(90)

turtle.end_fill()

turtle.exitonclick()


