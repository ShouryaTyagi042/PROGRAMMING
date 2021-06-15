#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    a = max(arr)
    b = min(arr)
    m = []
    m.extend(arr)
    m.remove(b)
    n = []
    n.extend(arr)
    n.remove(a)
    max_ = sum(m)
    min_ = sum(n)
    print(str(max_) + ' ' + str(min_))


miniMaxSum([1, 2, 3, 4, 5])


# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)
