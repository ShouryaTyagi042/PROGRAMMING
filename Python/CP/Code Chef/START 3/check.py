arr2 = [3, 2]
res = []
arr_r = 'PFPFU'
f = 0
p = 0
for ch in arr_r:
    if ch == "F":
        f += 1
    elif ch == "P":
        p += 1

if f >= arr2[0]:
    res.append("1")
elif f >= arr2[0] - 1 and p >= arr2[1]:
    res.append("1")
else:
    res.append("0")
r = ""
print(r.join(res))
