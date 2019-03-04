'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #3
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user to choose sine, cosine or log wave 
  and output the graph of curve

OUTPUT to monitor:
  Turtle Graphics - graph of curve

INPUT from keyboard:
  sides_count (int) - number of sides of polygon







'''



# Explain purpose of program to user
# This program outputs the graph of sin, cos and log curve



import math
import turtle

wn = turtle.Screen()
wn.setworldcoordinates(0,-2,360,2)
wn.bgcolor('lightblue')
fred = turtle.Turtle()
fred.ht()
fred.penup()
fred.goto(0,10)
fred.pendown()
fred.goto(0,-10)
fred.penup()
fred.goto(0,0)
fred.pendown()
fred.goto(360,0)
fred.penup()
fred.speed(0)



def main():

  print("This Program draws a sine, cosine, or log wave as requested by user")
  print("Would you like to draw a sin, cos, or log curve?")
  
  graph = input("Enter <sin>, <cos>, or <log>:     ")
  fred.pencolor('red')
  
  if graph == "sin":
      fred.penup()
      fred.goto(0,0)
      fred.pendown()
      for angle in range(360):
         y = math.sin(math.radians(angle))
         fred.goto(angle, y)
         
  elif graph == "cos":
      fred.penup()
      fred.goto(0,1)
      fred.pendown()
      for angle in range(361):
         y = math.cos(math.radians(angle))
         fred.goto(angle, y)
         
  elif graph == "log":
      wn.setworldcoordinates(0,-2,361,10)
      fred.penup()
      fred.goto(0,-2)
      fred.pendown()
      for x in range(1, 361, 5):
         y = math.log2(x)
         fred.goto(x, y)

  else:
    print("Invalid input: Cannot draw " + graph + " curve!")
    
  

  
  wn.exitonclick()
main() 

