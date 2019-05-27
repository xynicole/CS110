import turtle
import random
import time

BATCH_OF_DARTS=5000
BOARD_WIDTH=2
RIGHT_ANGLE=90

def drawSquare(t, width,top_left_x,top_left_y):
    t.penup()
    t.setpos(top_left_x,top_left_y)
    t.pendown()
    sides=4
    for i in range(sides):
        t.forward(BOARD_WIDTH)
        t.right(RIGHT_ANGLE)

def drawLine(t,x_start,y_start,x_end,y_end):
    t.penup()
    t.setpos(x_start,0)
    t.pendown()
    t.goto(x_end,0)
    t.goto(0,0)
    t.goto(0,y_start)
    t.goto(0,y_end)
    


def drawCircle(t,radius):
    t.penup()
    t.setpos(0,-1)
    t.pendown()
    t.circle(1,steps=360)
    t.penup()

def setUpDartboard(screen,t):
    screen.setworldcoordinates(-2,-2,2,2)
    drawSquare(t,2,-1,1)
    drawLine(t,-1.5,1.5,1.5,-1.5)
    drawCircle(t,1)

def throwDart(t):
    t.penup()
    t.home()
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    t.goto(x,y)
    t.shape("circle")
    
    if t.distance(0,0)<=1:
        t.color("blue")
    else:
        t.color("orange")
    t.stamp()    

def inCircle(t, circle_center, radius):
    circle_center=(0,0)
    radius=1
    if t.distance(circle_center)<=radius:
        return True
    else:
        return False
        


def montePi(t, num_darts):
   
    insideCount=0
    if (inCircle==True):
        insideCount+=1
    else:
        insideCount+=0
    return insideCount
    montePi=(insideCount/BATCH_OF_DARTS)*4
    return montePi

def main():
    #Create window, turtle,set up window as dartboard
    window=turtle.Screen()
    t=turtle.Turtle()
    turtle.speed(100)
    setUpDartboard(window,t)

    #Loop for 10 darts to test your code
    for i in range(10):
        throwDart(t)
    
    window.tracer(BATCH_OF_DARTS)
    #Conduct simulation and print result
    number_darts=int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi=montePi(number_darts,t)
    print("\nThe estimation of pi using "+str(number_darts)+"virtual darts is " +str(approx_pi))
    print("\tPart B Complete...")
    window.exitonclick()
main()


    
