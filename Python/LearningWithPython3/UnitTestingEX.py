import sys
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def turn_clockwise(direction) :
    """ Takes Direction in N S E W format
         and returns its next compass point
         in the clockwise direction. """
    if direction == "N" :
        return "E"
    elif direction == "S" :
        return "W"
    elif direction == "E" :
        return "S"
    elif direction == "W" :
        return "N"
    else :
        return None

def day_name(num) :

    if num in range(7) :
        return days[num]
    else :
        return None

def day_num(day) :
    if day in days :
        return days.index(day)
    else :
        return None

def day_add(day,delta) :
    add = delta % 7
    day_numb = day_num(day)
    ans = (day_numb + add) % 7
    return day_name(ans)


def test(did_pass) :
    """ Print the result of the case"""
    linenum = sys._getframe(1).f_lineno
    if did_pass :
        msg = "Test at line {} ok.".format(linenum)
    else :
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()

