t = int(input())
for i in range(t):
    x = int(input())
    n = x*3
    l3 = []
    l1 = []
    d1 = {}
    for i in range(n) :
        l = list(map(str, input().rstrip().split()))
        l1.append(l[0])
        d1[i] = l
    l4 = set(l1)
    # print(l4)
    for ch in l4 :
        res = 0
        for j in range(n) :
            if ch == l1[j] :
                res += int(d1[j][1])
        l3.append(res)

    l3.sort()
    print(*l3)


