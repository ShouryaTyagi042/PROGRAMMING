import sys
from UnitTesting import *
# import os
# print(os.getcwd())
def add_vectors(l1,l2) :
    l3 = []
    x = len(l2)
    for i in range(x) :
        l3.append( l1[i] + l2[i] )
    return l3
def scalar_mult(s, v) :
    l = []
    for i in v :
        l.append(s*i)
    return l

def cross_product(u, v) :
    """ Finds out the dot product where u and v are vectors """
    l = []
    l.append(u[1]*v[2]-u[2]*v[1])
    l.append(-(v[2]*u[0]-v[0]*u[2]))
    l.append(u[0]*v[1]-v[0]*u[1])
    return l



def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(cross_product([1,2,3],[4,5,6])==[-3,6,-3])
test_suite()
