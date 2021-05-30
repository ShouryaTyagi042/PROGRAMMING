t = int(input())
i = 0
l2 = []
for i in range(0, t):
    n, k = input().split(" ")
    n = int(n)
    k = int(k)
    sum_ = n + k
    l2.append(sum_)
for ch in l2:
    print(ch)
