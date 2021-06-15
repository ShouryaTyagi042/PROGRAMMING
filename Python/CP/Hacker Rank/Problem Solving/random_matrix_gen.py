import random
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
random.shuffle(l1)
r1 = l1[0:3]
r2 = l1[3:6]
r3 = l1[6:]
matrix = []
matrix.append(r1)
matrix.append(r2)
matrix.append(r3)
print(matrix)


4 9 2
3 5 7
8 1 5
