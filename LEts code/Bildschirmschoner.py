from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(1200):
    color('green')
    circle(i)
    color('white')
    circle(i*0.8)
    right(1)
    forward(1)
done()