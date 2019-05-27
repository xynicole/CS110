import turtle
import random
def main():
    window=turtle.Screen()
    window.bgcolor("lightblue")
    michelangelo=turtle.Turtle()
    leonardo=turtle.Turtle()
    michelangelo.color("orange")
    leonardo.color("blue")
    michelangelo.shape("turtle")
    leonardo.shape("turtle")

    michelangelo.up()
    leonardo.up()
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)

    michelangelo.forward(random.randrange(1,300))
    leonardo.forward(random.randrange(1,300))
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)

    michelangelo.forward(random.randrange(0,30))
    leonardo.forward(random.randrange(0,30))
    michelangelo.forward(random.randrange(0,30))
    leonardo.forward(random.randrange(0,30))
    michelangelo.forward(random.randrange(0,30))
    leonardo.forward(random.randrange(0,30))
    michelangelo.forward(random.randrange(0,30))
    leonardo.forward(random.randrange(0,30))
    michelangelo.forward(random.randrange(0,30))
    leonardo.forward(random.randrange(0,30))
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)

    
    leonardo.down()
    leonardo.setheading(60)
    leonardo.forward(50)
    leonardo.setheading(300)
    leonardo.forward(50)
    leonardo.setheading(180)
    leonardo.forward(50)


    leonardo.forward(50)
    leonardo.right(90)
                        


    window.exitonclick()
main()
