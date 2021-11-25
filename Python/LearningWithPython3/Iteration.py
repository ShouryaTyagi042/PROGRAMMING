import sys
def sum_to_n(i) :
    """ Finds out the sum till i ,
    where i is the given integer
    ex. 1+2+3+---i
    """
    ad = 0
    ts = 0
    while ad <= i :
        ts += ad
        ad += 1
    return ts

# print(sum_to_n(5))

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
    test(sum_to_n(5)==15)


test_suite()

