
import random
import math
import turtle

def main():

    tyr = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-2,-2,2,2)
    tyr.hideturtle()
    
    tyr.penup()
    tyr.goto(-1,-1)
    tyr.pendown()
    tyr.goto(-1,1)
    tyr.goto(1,1)
    tyr.goto(1,-1)
    tyr.goto(-1,-1)
    tyr.goto(-1,0)
    tyr.goto(1,0)
    tyr.penup()
    tyr.goto(0,1)
    tyr.pendown()
    tyr.goto(0,-1)
    tyr.penup()
    reddart = 0
    
    print("This program simulates throwing darts at a datboard to simulate pi")
    print()
    dart_num = input("Please input the number of darts to be thrown"
                       "in the simulation:  ")
    dart_int = int(dart_num)
    wn.tracer(1000)
    for i in range(dart_int):
        randx = random.random()
        randy = random.random()
        x = randx * random.choice([-1,1])
        y = randy * random.choice([-1,1])
        tyr.goto(x,y)
        if tyr.distance(0,0) <= 1:
            tyr.color('red')
            reddart = reddart + 1
        else:
            tyr.color('blue')
        tyr.dot()


    pi = (reddart / dart_int) * 4

    print(pi)



main()
