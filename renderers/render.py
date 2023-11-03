import turtle
from MatrixObj import Matrix
from math import sin, cos, radians

turtle.title(f'Render 1 | Matricies                                                    ')
turtle.Screen().cv._rootwindow.resizable(False, False)
turtle.Screen().setup(800, 500)
turtle.colormode(255)
turtle.tracer(0, 0)
p=turtle.Turtle()
p.hideturtle()
p.speed(0)
p.penup()
o=turtle.Turtle()
o.hideturtle()
o.speed(0)
o.penup()
o.color((255, 10, 50))

S=50
A=45
point=Matrix('2x1', [[2],[0]])*S
rotation=Matrix('2x2',[[cos(radians(A)),-sin(radians(A))],[sin(radians(A)),cos(radians(A))]])
#rotation=Matrix('2x2',[[4,0],[4,1]])
rotated=rotation@point

p.goto(0,0)
p.pendown()
p.goto(point.matrix[0][0],point.matrix[1][0])

o.goto(0,0)
o.pendown()
o.goto(rotated.matrix[0][0],rotated.matrix[1][0])

turtle.update()
turtle.exitonclick()
