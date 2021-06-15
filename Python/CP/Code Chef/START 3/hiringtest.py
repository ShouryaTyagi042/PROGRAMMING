t = int(input())
# res = []
for i in range(t):
    res = []
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = list(map(int, input().rstrip().split()))
    # arr3 = list(map(int, input().rstrip().split()))

    for c in range(arr1[0]):
        arr_r = input()
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
