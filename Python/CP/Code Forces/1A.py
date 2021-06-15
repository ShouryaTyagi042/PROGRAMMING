arr = list(map(int, input().rstrip().split()))
# print(arr)
a1 = 0
a2 = 0
if arr[0] % arr[2] != 0:
    s = arr[0] // arr[2] + 1
    a1 += s
elif arr[0] % arr[2] == 0:
    s = arr[0] // arr[2]
    a1 += s
if arr[1] % arr[2] == 0:
    s = arr[1] // arr[2]
    a2 += s
elif arr[1] % arr[2] != 0:
    s = arr[1] // arr[2] + 1
    a2 += s
print(a1 * a2)
