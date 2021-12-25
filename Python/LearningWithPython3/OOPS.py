from math import sqrt
from UnitTesting import test
class Point :
    def __init__(self,x=0,y=0) :
        self.x = x
        self.y = y
    """ Addition of new method distance from origin """
    def distance_from_origin(self) :
        return(((self.x**2)+(self.y**2))**0.5)
# Instances as arguements and parameters
    def print_point(pt) :
        print("({},{})".format(pt.x,pt.y))
# Converting an instance to a string
    def __str__(self) :
        return"({},{})".format(self.x,self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    def area (self) :
        return self.width*self.height
    def perimeter(self) :
        return 2*(self.width + self.height)
    def flip(self) :
        width = self.width
        self.width = self.height
        self.height = width
    def contains(self,target) :
        if self.corner.x < target.y < (self.corner.x + self.width) and (self.corner.y - self.height) < target.y < self.corner.y :
            return True


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
print(bomb.area())
print(box.perimeter())
print(box)
box.flip()
print(box)

r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))













