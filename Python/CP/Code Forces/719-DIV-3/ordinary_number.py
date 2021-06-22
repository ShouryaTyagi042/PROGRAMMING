t = int(input())
for i in range(t) :
    n = int(input())
    i = 1
    res = 0
    while i <= n :
        for j in range(1,10) :
            if i * j <= n :
                res += 1
        i = i*10 + 1
    print(res)
