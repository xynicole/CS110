import turtle
import math



def drawer(t,height,letter):
    t.fillcolor('red')
    t.begin_fill()
    t.left(90)               
    t.forward(height)
    t.write("%s: %d" % (letter, height))
    t.right(90)
    t.forward(4)      
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
def count_all(text):
    count = 0
    d = {}
    for c in text:
      if c == ' ':
          c = "SPACE"
      if c in d:
        d[c] = d[c] + 1
      else:
        d[c] = 1

    return d

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.bgcolor('lightgreen')

    my_str = input('Enter text:  ')
    dictionary = count_all(my_str)
    keys = list(dictionary.keys())
    max_height = max(dictionary.values())
    wn.setworldcoordinates(-1,-1, len(keys)*4 + 2, max_height +2)
    
    keys.sort()
    for k in keys:
        print("%s: %d" % (k, dictionary[k]))
        drawer(t,dictionary[k], k)

main()
