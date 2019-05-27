import Point



class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.__location = initP
        self.__width = initW
        self.__height = initH

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)

    def __str__(self):
        return "point = %s \n" + str(self.__location) \
               + "height = %d \n"  +str (self.__height) \
               + "width = %d \n" +str(self.__width) \
               + "area = %d \n" +str(self.area()) \
               + "perimether = %d \n" +str(self.perimeter())
def main():
        pt = point.Point(4,8)
        r = Rectangle(pt,8,8)
        print(r)
        
        
    
