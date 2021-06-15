def merge_the_tools(string, k):

    # your code goes here

    # string = "AAAABCADDDEF"
    # k = 4
    a = []
    res = []
    no_cut = len(string) // k
    start = 0
    end = k
    for i in range(no_cut):
        a.append(string[start:end])
        start += k
        end += k
    # print(a)
    for cut in a:
        l = list(cut)
        resl = []
        for ch in l:
            if ch not in resl:
                resl.append(ch)
        sep = ""
        ans = sep.join(resl)
        res.append(ans)
    for o in res:
        print(o)
    # print(l)

    # merge_the_tools("AAABCADDE", 3)
