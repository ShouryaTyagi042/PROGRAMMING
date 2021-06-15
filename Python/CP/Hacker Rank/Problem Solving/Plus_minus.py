#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    d = len(arr)
    p = 0
    n = 0
    z = 0
    for ch in arr:
        if ch > 0:
            p += 1
        elif ch < 0:
            n += 1
        else:
            z += 1
    rp = p / d
    rn = n / d
    rz = z / d
    return rp
    return rn
    return rz


if __name__ == '__main__':
    # n = int(input())

    arr = list(map(int, input().rstrip().split()))


print(plusMinus(arr))
