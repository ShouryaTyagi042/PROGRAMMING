import sys

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def test(did_pass) :
    """ Print the result of the case"""
    linenum = sys._getframe(0).f_lineno
    if did_pass :
        msg = "Test at line {} ok.".format(linenum)
    else :
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)

def undo_absolute() :
    check = absolute_value(-5)
    return -check


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite()



