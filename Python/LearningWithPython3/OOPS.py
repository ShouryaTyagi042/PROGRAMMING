from math import sqrt
class Point:
    """ Point class represents and manipulates x,y coords. """
    def __init__(self):

        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()
q = Point()
print(p.x,p.y)
print(q.x,q.y)

p.x = 4
p.y = 5

print("(x={0},y={1})".format(p.x,p.y))
# distance_from_origin = math.sqrt(p.x*p.x + p.y*p.y)

class APoint :
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






p1 = APoint(3,4)
print(p1.distance_from_origin())
p1.print_point()
str(p1)
print(p1)






