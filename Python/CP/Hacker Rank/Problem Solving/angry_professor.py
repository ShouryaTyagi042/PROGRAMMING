#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.


def angryProfessor(k, a):
    # print(a)
    # print(b)
    c = "YES"
    b = 'NO'
    thresh = 0
    for i in range(len(a)):
        if int(a[i]) > 0:
            continue
        else:
            thresh += 1
    if thresh >= k:
        return b
    else:
        return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
