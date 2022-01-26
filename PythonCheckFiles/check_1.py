def count(sub,st) :
    step = 0
    c = 0
    l = len(sub)
    while True :
        s = st[step:].find(sub)
        if s != -1 :
            c += 1
            step += s + 1
        else :
            break
    return c
print(count("aaa", "aaaaaa"))
