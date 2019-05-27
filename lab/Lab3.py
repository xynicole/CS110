def main():

  import math
  import turtle

  wn = turtle.Screen()
  wn.setworldcoordinates(0,-2,360,2)
  wn.bgcolor('lightblue')
  fred = turtle.Turtle()
  fred.ht()
  fred.penup()
  fred.goto(0,2)
  fred.pendown()
  fred.goto(0,-2)
  fred.penup()
  fred.goto(0,0)
  fred.pendown()
  fred.goto(360,0)
  fred.penup()

  #ask user 
  sincos = input("Enter the sine wave or cosine wave:     ")


  if sincos == "sine":
      for angle in range(360):
         y = math.sin(math.radians(angle))
         fred.goto(angle, y)
  elif sincos == "cosine":
      fred.penup()
      fred.goto(0,1)
      fred.pendown()
      for angle in range(360):
         y = math.cos(math.radians(angle))
         fred.goto(angle, y)
  else:
    print('Invalid input')
      

    

  wn.exitonclick()
main()
