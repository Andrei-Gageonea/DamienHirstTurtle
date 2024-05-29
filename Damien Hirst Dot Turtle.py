import random
import colorgram
import turtle as turtle
from turtle import *
import random as r
turtle.colormode(255)
beast = Turtle()
beast.speed(30)
turtle.colormode(255)
colors = colorgram.extract(r'C:\Users\gandr\Desktop\Programmer Shit\100 Days Python\Day 18\colors.jpeg', 10)
beast.penup()
beast.setposition(-400,-300)
def random_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return (r,g,b)

def going():
    global colors
    #color = random.choice(colors) #For random colors extracted from the picture
    #color = color.rgb
    color = random_color() #For completely random colors
    beast.color(color)
    beast.begin_fill()
    beast.circle(20)
    beast.end_fill()
    beast.forward(60)


for _ in range(1,11):

    for __ in range(1,11):
        going()

    beast.begin_fill()
    beast.circle(20)
    beast.end_fill()

    beast.left(90)
    beast.forward(50)
    beast.right(90)
    beast.back(600)



screen = Screen()
screen.exitonclick()