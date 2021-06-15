#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.


def staircase(n):
    for i in range(1, n + 1):
        for j in range(0, n - i):
            print(" ", end="")
        for k in range(0, i + 1):
            if k < i:

                print("#", end="")
            elif k == i:
                print("")


# staircase(5)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
