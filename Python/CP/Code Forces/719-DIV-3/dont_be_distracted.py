t = int(input())
for i in range(t):
    x = int(input())
    y = input()
    flag = False
    for i in range(x):
        for j in range(i, x):
            if y[i] == y[j]:
                continue
            else:
                s = y[j + 1:x]
                if y[i] in s:
                    flag = True
    if flag == True:
        print("NO")
    else:
        print("YES")
