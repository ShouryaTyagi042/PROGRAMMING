t = int(input())
for i in range(t):
    x = int(input())
    y = list(map(int, input().rstrip().split()))
    ans = 0
    for i in range(x):
        for j in range(i, x):
            if y[j] - y[i] == j - i:
                ans += 1
    print(ans - x)
