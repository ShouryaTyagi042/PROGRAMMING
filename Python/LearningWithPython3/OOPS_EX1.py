import turtle
class Point :
    def __init__(self,x=0,y=0) :
        self.x = x
        self.y = y

    def __str__(self) :
        return "({},{})".format(self.x,self.y)

    def distance(self,target) :
        return ((self.x-target.x)**2 + (self.y-target.y)**2)**0.5

    def reflect_x(self) :
        my = -self.y
        return Point(self.x,my)

    def slope_from_origin(self) :
        return (self.y/self.x)

    def equation_of_line(self,target) :
        """ y = mx + a  equation of line
            where m is the slope of the line
            a is a constant or intercept on y axis
         """
        m = (self.y-target.y)/(self.x-target.x)
        a = target.y - (m*target.x)
        return "y = {}x + {}".format(m,a)

# p1 = Point(3,4)
# p2 = Point(6,0)
# d = p1.distance(p2)
# print(d)
# p1_x = Point.reflect_x(p1)
# print(p1_x)
# print(p1.slope_from_origin())
# # print(Point.slope_from_origin(p1)) Two ways to call the method



# print(p1.equation_of_line(p2))





