#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    fall = range(s, t + 1)
    apple = a
    orange = b
    na = 0
    no = 0
    for i in range(0, len(apples)):
        apples[i] = apples[i] + a
    for i in range(0, len(oranges)):
        oranges[i] = oranges[i] + b
    for ch in apples:
        if ch in fall:
            na += 1
    for ch in oranges:
        if ch in fall:
            no += 1
    print(na)
    print(no)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
