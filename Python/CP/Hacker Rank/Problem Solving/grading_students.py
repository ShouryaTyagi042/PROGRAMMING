#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    l = []
    for ch in grades:
        if ch < 40:
            l.append(ch)
        elif ch == 100:
            l.append(ch)
        else:
            grade = str(ch)
            if int(grade[1]) > 5:
                tens = int(grade[0]) + 1
                roundof = tens * 10
            elif int(grade[1]) <= 5:
                tens = int(grade[0])
                roundof = tens * 10 + 5
            if roundof - ch < 3:
                l.append(roundof)
            else:
                l.append(ch)
    return l


# l1 = [73, 67, 38, 33]
# result = gradingStudents(l1)
# print(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
