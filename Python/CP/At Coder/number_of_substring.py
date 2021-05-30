s = list(input())
l = len(s)
res = []
ans = 0
for i in range(l):
    for j in range(i, l):
        res.append(s[i:j + 1])
a = set(res)
print(len(a))
