from turtle import *
t = Turtle()
t.forward(1)
while t.pos() < (200,0):
    t.forward(1)
    if t.pos() == (200, 0):
        break
t.rt(90)
while t.pos() < (200,200):
    t.forward(1)
    if t.pos() == (200, -200):
        break
t.rt(90)
while t.pos() > (0, -200):
    t.forward(1)
    if t.pos() == (0, -200):
        break
t.rt(90)
while t.pos() < (0,0):
    t.forward(1)
    if t.pos() == 1:
        break
t.lt(90)



