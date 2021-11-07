#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1 = s.replace(" ","-")
    l = list(s1.split())
    ans = []
    for w in l :
        if w[0].isalpha() == True :
            z = w.capitalize()
            ans.append(z)
        else  :
            ans.append(w)
    a = "".join(ans)
    a1 = a.replace("-"," ")
    return a1




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
