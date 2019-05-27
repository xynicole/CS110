class Point:

    def __init__(self, initX, initY):
        self.__x = initX
        self.__y = initY

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distanceFromOrigin(self):
        return ((self.__x ** 2) + (self.__y ** 2)) ** 0.5

    def __str__(self):
        return "x= %d, y= %d" % (self.__x, self.__y)

    def halfway(self, target):
         mx = (self.__x + target.x) / 2
         my = (self.__y + target.y) / 2
         return Point(mx, my)

##p = Point(3, 4)
##q = Point(5, 12)
##mid = p.halfway(q)
##
##print(mid)
##print(mid.getX())
##print(mid.getY())
