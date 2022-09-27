# Bibliothèques Python 


import turtle as tl
from random import randint
from os import system

fcolor=("violet", "red", "green", "yellow", "orange")
def pentagone(x, y, c):
    a = 72
    tl.penup()
    tl.goto(x, y)  
    tl.pendown()     
    tl.fillcolor("violet")
    tl.begin_fill()
    for i in range(5):
        tl.right(a)
        tl.forward(1.6*c)
        tl.left(180-a/2)
        tl.forward(1.6*c)
        #tl.right(a)
        #tl.forward(1.6*c)
    tl.end_fill()

    tl.fillcolor("white")
    tl.begin_fill()
    #tl.penup()
    #tl.goto(x+c/3, y+c/3)
    tl.pendown()
    for i in range(5):
        tl.forward(c)
        tl.left(a)
    tl.end_fill()



#pentagone(-100,-100,120)



def star(x, y, a,c, fc):
    
    tl.penup()
    tl.goto(x,y)

    tl.left(2*a)
    
    tl.fillcolor(fc)
    tl.pendown()

    tl.begin_fill()
    for i in range(5):
        tl.forward(c)
        tl.left(180-a)
    tl.end_fill()
    tl.penup()

tl.speed(0)
for k in range(100):
    i = randint(0, 4)
    x = randint(-100, 100)
    y = randint(-100, 100)
    c = randint(50, 100)
    star(x, y, 36,c, fcolor[i])
tl.done()

