i1 = input()
arr_1 = list(map(int, input().rstrip().split()))
res = []
# for ch in arr:
#     if ch not in res:
#         res.append(ch)
arr_a = set(map(int, input().rstrip().split()))
arr_b = set(map(int, input().rstrip().split()))
ans = 0
for ch in arr_1:
    if ch in arr_a:
        ans += 1
    elif ch in arr_b:
        ans -= 1
print(ans)
