import turtle
from MatrixObj import Matrix
from math import sin, cos, radians

turtle.title(f'Render 1 | Matricies                                                    ')
turtle.Screen().cv._rootwindow.resizable(False, False)
turtle.Screen().setup(800, 500)
turtle.colormode(255)
#turtle.tracer(0, 0)
p=turtle.Turtle()
p.hideturtle()
p.speed(0)
p.penup()

def draw_line(x,y):
    p.penup()
    p.goto(0,0)
    p.pendown()
    p.goto(x,y)

S=100
A=0
pointx=Matrix('3x1', [[1],[0],[0]])*S
pointy=Matrix('3x1', [[0],[1],[0]])*S
pointz=Matrix('3x1', [[0],[0],[1]])*S

rotation=Matrix('3x3',[[cos(radians(A)),0,-sin(radians(A))],[0,1,0],[sin(radians(A)),0,cos(radians(A))]])
rx=rotation@pointx
ry=rotation@pointy
rz=rotation@pointz

p.color('black')
draw_line(rx.matrix[0][0],rx.matrix[1][0])
p.color('red')
draw_line(ry.matrix[0][0],ry.matrix[1][0])
p.color('blue')
draw_line(rz.matrix[0][0],rz.matrix[1][0])

turtle.update()
turtle.exitonclick()