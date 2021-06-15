#!/bin/python3

import os
import sys
import datetime

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    a = len(s)
    am_or_pm = s[a - 2:]
    # print(am_or_pm)
    partial = s[2:a - 2]
    # print(partial)
    val = int(s[:2])
    if am_or_pm == "AM" and val == 12:
        val = "00"
        # print(str(val) + partial)

    elif am_or_pm == "PM" and val != 12:
        val += 12
    ans = str(val) + partial
    return ans


# n = timeConversion("07:05:45AM")
# print(n)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
