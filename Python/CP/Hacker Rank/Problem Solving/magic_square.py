#!/bin/python3

import math
import os
import random
import re
import sys
# matrix = [[5,3,4],[1,5,8],[6,4,2]]

# Complete the formingMagicSquare function below.
def random_matrix():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    random.shuffle(l1)
    r1 = l1[0:3]
    r2 = l1[3:6]
    r3 = l1[6:]
    matrix = []
    matrix.append(r1)
    matrix.append(r2)
    matrix.append(r3)
    return matrix
m = [[4,9,2],[3,5,7],[8,1,5]]

def formingMagicSquare(s):
    # m1 = [[4,9,2],[3,5,7],[8,1,6]]
    # m2 = [[2,7,6],[9,5,1],[4,3,8]]
    # m3 = [[6,1,8],[7,5,3],[2,9,4]]
    # m4 = [[8,3,4],[1,5,9],[6,7,2]]
    # m5 = [[2,9,4],[7,5,3],[6,1,8]]
    # m6 = [[6,7,2],[1,5,9],[8,3,4]]
    # m7 = [[8,1,6],[3,5,7],[4,9,2]]
    # m8 = [[4,3,8],[9,5,1],[2,7,6]]
    c = [[[4,9,2],[3,5,7],[8,1,6]],[[2,7,6],[9,5,1],[4,3,8]],[[6,1,8],[7,5,3],[2,9,4]],[[8,3,4],[1,5,9],[6,7,2]],[[2,9,4],[7,5,3],[6,1,8]],[[6,7,2],[1,5,9],[8,3,4]],[[8,1,6],[3,5,7],[4,9,2]],[[4,3,8],[9,5,1],[2,7,6]]]
    l = []
    for k in range(8):
        # w = []
        # cor = []b
        ans  = 0
        for i in range(3):
            for j in range(3):
                if s[i][j] == c[k][i][j]:
                    continue
                else:
                    ans += abs(int(s[i][j])-int(c[k][i][j]))
        l.append(ans)
                    # w.append(int(s[i][j]))
                    # cor.append(int(c[k][i][j]))
        # ans = 0
        # for i in range(len(w)):
        #     ans += abs(w[i] - cor[i])
        #     l1.append(ans)
    a = min(l)
    print(a)
    print(l)

# formingMagicSquare(random_matrix())
formingMagicSquare(m)



# result = formingMagicSquare(matrix)
# print(result)
# print(l)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = []

#     for _ in range(3):
#         s.append(list(map(int, input().rstrip().split())))

#     result = formingMagicSquare(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
