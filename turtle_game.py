from turtle import *
tess = Turtle()
tess.forward(1)
while tess.pos() < (200,0):
    tess.forward(1)
    if tess.pos() == (200, 0):
        break
tess.rt(90)
while tess.pos() < (200,200):
    tess.forward(1)
    if tess.pos() == (200, -200):
        break
tess.rt(90)
while tess.pos() > (0, -200):
    tess.forward(1)
    if tess.pos() == (0, -200):
        break
tess.rt(90)
while tess.pos() < (0,0):
    tess.forward(1)
    if tess.pos() == 1:
        break
tess.lt(90)



