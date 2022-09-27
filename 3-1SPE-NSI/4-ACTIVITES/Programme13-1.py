
from turtle import *
from math import pi, sin


def motif (x, y, a, e, cl1, cl2):
    up()
    goto(x,y)
    pensize(2)
    speed(1)
    down()
    color("black")
    forward(a)
    left(120)
    forward(a)
    right(90)
    circle(a, 300)
    right(90)
    forward(a)
    goto(x,y)
    up()
    goto(x, y+ e + a*sin(pi/3))
    down()
    setheading(0)
    color(cl1)
    fillcolor(cl2)
    begin_fill()
    circle(a - 2*e)
    end_fill()
  



motif(0,0,100,10, "red", "green") 

motif(50,15,80,5, "blue", "red")

motif(-50,-100,60,5, "green", "grey")

done() 

