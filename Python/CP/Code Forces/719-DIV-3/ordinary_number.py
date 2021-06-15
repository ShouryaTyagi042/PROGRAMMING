t = int(input())
for i in range(t):
    x = int(input())
    ans = 0
    for i in range(1, x + 1):
        a = str(i)
        if a[0] not in a[1:]:
            continue
