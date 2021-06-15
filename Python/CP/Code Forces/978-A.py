t = int(input())
arr = list(map(str, input().rstrip().split()))
res = []
for i in range(len(arr)):
    if arr[-1] not in res:
        a = arr.pop()
        res.append(a)
    else:
        arr.pop()
res.reverse()
st = " "
print(len(res))
print(st.join(res))
