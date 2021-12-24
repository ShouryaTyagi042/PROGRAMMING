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
list_of_messages = []
class SMS_store :
    def __init__(self,has_been_viewed=False, from_number="NA", time_arrived="NA", text_of_SMS="NA") :
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS) :
        message = (False,from_number, time_arrived, text_of_SMS)
        list_of_messages.append(message)

    def message_count(self) :
        return len(list_of_messages)

    def get_unread_message(self) :
        unread = []
        for i in list_of_messages :
            if i[0] == False :
                unread.append(list_of_messages.index(i))
        return unread

    def get_message(self,i) :
        if i >= len(list_of_messages) :
            return None
        else :
            message_unread = list_of_messages[i]
            message_read = (True,message_unread[1],message_unread[2],message_unread[3])
            list_of_messages.pop(i)
            list_of_messages.insert(i,message_read)
            return message_read


    def clear(self) :
        list_of_messages.clear()

    def delete(self,i) :
        list_of_messages.pop(i)

my_inbox = SMS_store()
# print(my_inbox.text_of_SMS)
my_inbox.add_new_arrival("9871955895","13:00","Hey There I am using Whatsapp")
my_inbox.add_new_arrival("8527787467","13:00","Hey There I am Rajni Tyagi")
my_inbox.add_new_arrival("8800798964","13:00","Hey There I am Shourya Tyagi")
my_inbox.add_new_arrival("7838346721","13:00","Hey There I am Jai Bhagwan Tyagi")

print(my_inbox.message_count())
print(my_inbox.get_unread_message())
print(my_inbox.get_message(2))
print(my_inbox.get_unread_message())
# print(list_of_messages)











