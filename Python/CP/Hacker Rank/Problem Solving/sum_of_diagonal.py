#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    l = 0
    r = 0
    for i in range(0, len(arr)):
        l += int(arr[i][i])
        r += int(arr[len(arr) - i - 1][i])

        # print(r)
    ans = abs(l - r)
    return ans

# sample input given in the below line
# diagonalDifference([[11, 2, 4], [4, 5, 6, ], [10, 8, -12]])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
