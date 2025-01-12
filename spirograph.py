from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed('fastest')

screen = Screen()
screen.colormode(255)

def random_colour():
    r = random.choice(range(1,255))
    g = random.choice(range(1,255))
    b = random.choice(range(1,255))
    return (r,g,b)



def draw_spirograph():
    a = 36
    while a > 0:
        timmy.color(random_colour())
        timmy.circle(100.0)
        timmy.right(10)
        a -= 1


draw_spirograph()


screen.exitonclick()