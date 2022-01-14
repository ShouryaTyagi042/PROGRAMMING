"""
/* what i was trying
# !/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    # rec = {}
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        # rec[x] = arr[x]

    k = int(input())
rec = {}
for x in range(n) :
    rec[tuple(arr[x])] = arr[x][k]
print(sorted(rec.values()))

# print(rec.keys().sort())
# for i in sorted(rec.keys()) :
#     for x in range(m) :
#         print(rec[i][x],end=" ")
#     print(" ")

# 5 3
# 10 2 5
# 7 2 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
*/
"""
# !/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N, M = map(int, input().split())
    rows = [input() for _ in range(N)]
    K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)
