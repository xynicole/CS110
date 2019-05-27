import point



class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.__location = initP
        self.__width = initW
        self.__height = initH



    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)

    def __str__(self):
        return "point = %s \nheight = %d \nwidth = %d \narea = %d \nperimeter = %d \n"\
               % (self.__location, self.__height, self.__width, self.area(), self.perimeter())
def main():
        pt = point.Point(4,8)
        r = Rectangle(pt,8,8)
        print(r)
main()
        
        
    
